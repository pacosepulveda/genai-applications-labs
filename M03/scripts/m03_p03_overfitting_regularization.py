from pathlib import Path
import copy

import numpy as np
import pandas as pd
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

torch.manual_seed(42)
np.random.seed(42)


def locate(path_candidates):
    for p in path_candidates:
        p = Path(p)
        if p.exists():
            return p
    raise FileNotFoundError(path_candidates)


df = pd.read_csv(locate([
    "../assets/intent_requests.csv",
    "M03/assets/intent_requests.csv",
    "../../M03/assets/intent_requests.csv",
]))

train_df, val_df = train_test_split(
    df,
    test_size=0.35,
    random_state=42,
    stratify=df["label"],
)

# Reducimos train de manera estratificada para provocar overfitting.
train_small, _ = train_test_split(
    train_df,
    train_size=0.30,
    random_state=42,
    stratify=train_df["label"],
)

vectorizer = TfidfVectorizer(max_features=1500, ngram_range=(1, 2))
Xtr = vectorizer.fit_transform(train_small["request_text"]).toarray().astype("float32")
Xval = vectorizer.transform(val_df["request_text"]).toarray().astype("float32")

le = LabelEncoder()
ytr = le.fit_transform(train_small["label"])
yval = le.transform(val_df["label"])

train_loader = DataLoader(
    TensorDataset(torch.tensor(Xtr), torch.tensor(ytr, dtype=torch.long)),
    batch_size=32,
    shuffle=True,
)
val_loader = DataLoader(
    TensorDataset(torch.tensor(Xval), torch.tensor(yval, dtype=torch.long)),
    batch_size=64,
    shuffle=False,
)


class LargeMLP(nn.Module):
    def __init__(self, input_dim, n_classes, regularized=False):
        super().__init__()
        layers = [
            nn.Linear(input_dim, 512),
            nn.ReLU(),
        ]
        if regularized:
            layers.append(nn.Dropout(0.40))
        layers += [
            nn.Linear(512, 256),
            nn.ReLU(),
        ]
        if regularized:
            layers.append(nn.Dropout(0.30))
        layers.append(nn.Linear(256, n_classes))
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x)


def evaluate(model, loader, loss_fn):
    model.eval()
    losses, true, pred = [], [], []
    with torch.no_grad():
        for xb, yb in loader:
            logits = model(xb)
            losses.append(loss_fn(logits, yb).item())
            true.extend(yb.numpy())
            pred.extend(logits.argmax(1).numpy())
    return float(np.mean(losses)), f1_score(true, pred, average="macro")


def train(model, weight_decay=0.0, max_epochs=60, early_stopping=False, patience=6):
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=1e-3,
        weight_decay=weight_decay,
    )
    history = []
    best_state = None
    best_val = float("inf")
    bad_epochs = 0

    for epoch in range(1, max_epochs + 1):
        model.train()
        train_losses = []
        true, pred = [], []

        for xb, yb in train_loader:
            optimizer.zero_grad()
            logits = model(xb)
            loss = loss_fn(logits, yb)
            loss.backward()
            optimizer.step()

            train_losses.append(loss.item())
            true.extend(yb.numpy())
            pred.extend(logits.argmax(1).detach().numpy())

        train_loss = float(np.mean(train_losses))
        train_f1 = f1_score(true, pred, average="macro")
        val_loss, val_f1 = evaluate(model, val_loader, loss_fn)

        history.append({
            "epoch": epoch,
            "train_loss": train_loss,
            "val_loss": val_loss,
            "train_f1": train_f1,
            "val_f1": val_f1,
        })

        if val_loss < best_val - 1e-4:
            best_val = val_loss
            best_state = copy.deepcopy(model.state_dict())
            bad_epochs = 0
        else:
            bad_epochs += 1

        if early_stopping and bad_epochs >= patience:
            print("early stopping en epoch", epoch)
            break

    if early_stopping and best_state is not None:
        model.load_state_dict(best_state)

    return pd.DataFrame(history)


base_model = LargeMLP(Xtr.shape[1], len(le.classes_), regularized=False)
base_history = train(base_model, weight_decay=0.0, max_epochs=60)

reg_model = LargeMLP(Xtr.shape[1], len(le.classes_), regularized=True)
reg_history = train(
    reg_model,
    weight_decay=1e-3,
    max_epochs=60,
    early_stopping=True,
    patience=6,
)

plt.figure(figsize=(9, 5))
plt.plot(base_history["epoch"], base_history["train_loss"], label="base train")
plt.plot(base_history["epoch"], base_history["val_loss"], label="base validation")
plt.plot(reg_history["epoch"], reg_history["val_loss"], label="regularizada validation")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.legend()
plt.title("Overfitting y regularización")
plt.show()

# Gradient norm y clipping: una iteración demostrativa.
reg_model.train()
xb, yb = next(iter(train_loader))
optimizer = torch.optim.AdamW(reg_model.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()

optimizer.zero_grad()
loss = loss_fn(reg_model(xb), yb)
loss.backward()

before = torch.sqrt(sum(
    (p.grad.detach() ** 2).sum()
    for p in reg_model.parameters()
    if p.grad is not None
))
returned_norm = torch.nn.utils.clip_grad_norm_(reg_model.parameters(), max_norm=1.0)
after = torch.sqrt(sum(
    (p.grad.detach() ** 2).sum()
    for p in reg_model.parameters()
    if p.grad is not None
))

print("norma antes:", float(before))
print("norma reportada por clip_grad_norm_:", float(returned_norm))
print("norma después:", float(after))

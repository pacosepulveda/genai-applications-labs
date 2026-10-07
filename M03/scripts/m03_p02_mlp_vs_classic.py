from pathlib import Path
import json
import time

import joblib
import numpy as np
import pandas as pd
import torch
from scipy import sparse
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

torch.manual_seed(42)
np.random.seed(42)


def locate(path_candidates):
    for p in path_candidates:
        p = Path(p)
        if p.exists():
            return p
    raise FileNotFoundError(f"No encuentro ninguno de estos paths: {path_candidates}")


dataset_path = locate([
    "../assets/intent_requests.csv",
    "M03/assets/intent_requests.csv",
    "../../M03/assets/intent_requests.csv",
])

df = pd.read_csv(dataset_path)
features = [
    "request_text",
    "channel",
    "business_unit",
    "language",
    "urgency",
    "requires_authoritative_sources",
]

X_train_full, X_test, y_train_full, y_test = train_test_split(
    df[features],
    df["label"],
    test_size=0.20,
    random_state=42,
    stratify=df["label"],
)

X_train, X_val, y_train, y_val = train_test_split(
    X_train_full,
    y_train_full,
    test_size=0.20,
    random_state=42,
    stratify=y_train_full,
)

categorical = [
    "channel",
    "business_unit",
    "language",
    "urgency",
    "requires_authoritative_sources",
]


def build_preprocessor():
    return ColumnTransformer([
        ("text", TfidfVectorizer(max_features=1000, ngram_range=(1, 2)), "request_text"),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
    ])


# Baseline clásico
classic_pipeline = Pipeline([
    ("preprocessor", build_preprocessor()),
    ("model", LogisticRegression(max_iter=1000)),
])

classic_pipeline.fit(X_train, y_train)

t0 = time.perf_counter()
classic_pred = classic_pipeline.predict(X_test)
classic_latency_ms = (time.perf_counter() - t0) * 1000

classic_f1 = f1_score(y_test, classic_pred, average="macro")
classic_acc = accuracy_score(y_test, classic_pred)

print("CLASSIC")
print("macro F1:", round(classic_f1, 4))
print("accuracy:", round(classic_acc, 4))
print("latencia batch test (ms):", round(classic_latency_ms, 3))

# Preprocesamiento de la MLP
neural_preprocessor = build_preprocessor()
Xtr = neural_preprocessor.fit_transform(X_train)
Xval = neural_preprocessor.transform(X_val)
Xte = neural_preprocessor.transform(X_test)


def dense_float32(x):
    if sparse.issparse(x):
        return x.toarray().astype("float32")
    return np.asarray(x, dtype="float32")


Xtr = dense_float32(Xtr)
Xval = dense_float32(Xval)
Xte = dense_float32(Xte)

label_encoder = LabelEncoder()
ytr = label_encoder.fit_transform(y_train)
yval = label_encoder.transform(y_val)
yte = label_encoder.transform(y_test)

train_loader = DataLoader(
    TensorDataset(
        torch.tensor(Xtr, dtype=torch.float32),
        torch.tensor(ytr, dtype=torch.long),
    ),
    batch_size=64,
    shuffle=True,
)

val_loader = DataLoader(
    TensorDataset(
        torch.tensor(Xval, dtype=torch.float32),
        torch.tensor(yval, dtype=torch.long),
    ),
    batch_size=64,
    shuffle=False,
)


class NeuralIntentMLP(nn.Module):
    def __init__(self, input_dim, num_classes, hidden_dim=128):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, num_classes),
        )

    def forward(self, x):
        return self.network(x)


hidden_dim = 128
model = NeuralIntentMLP(
    input_dim=Xtr.shape[1],
    num_classes=len(label_encoder.classes_),
    hidden_dim=hidden_dim,
)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)


def evaluate(loader):
    model.eval()
    losses, y_true, y_pred = [], [], []

    with torch.no_grad():
        for xb, yb in loader:
            logits = model(xb)
            losses.append(loss_fn(logits, yb).item())
            y_true.extend(yb.cpu().numpy())
            y_pred.extend(logits.argmax(dim=1).cpu().numpy())

    return (
        float(np.mean(losses)),
        f1_score(y_true, y_pred, average="macro"),
        accuracy_score(y_true, y_pred),
    )


history = []
max_epochs = 8

for epoch in range(1, max_epochs + 1):
    model.train()

    for xb, yb in train_loader:
        optimizer.zero_grad()
        logits = model(xb)
        loss = loss_fn(logits, yb)
        loss.backward()
        optimizer.step()

    val_loss, val_f1, val_acc = evaluate(val_loader)
    history.append({
        "epoch": epoch,
        "val_loss": val_loss,
        "val_f1": val_f1,
        "val_acc": val_acc,
    })
    print(
        f"epoch={epoch:02d} "
        f"val_loss={val_loss:.4f} "
        f"val_f1={val_f1:.4f}"
    )

# Evaluación final sobre test
model.eval()
test_tensor = torch.tensor(Xte, dtype=torch.float32)

t0 = time.perf_counter()
with torch.no_grad():
    neural_logits = model(test_tensor)
neural_latency_ms = (time.perf_counter() - t0) * 1000

neural_pred = neural_logits.argmax(dim=1).cpu().numpy()
neural_f1 = f1_score(yte, neural_pred, average="macro")
neural_acc = accuracy_score(yte, neural_pred)

print("\nNEURAL")
print("macro F1:", round(neural_f1, 4))
print("accuracy:", round(neural_acc, 4))
print("latencia batch test (ms):", round(neural_latency_ms, 3))
print("parámetros:", sum(p.numel() for p in model.parameters()))

print("\nDECISIÓN")
if neural_f1 > classic_f1 + 0.02:
    print("El modelo neuronal mejora de forma visible; valorar USE_NEURAL.")
elif classic_f1 >= neural_f1:
    print("La evidencia no justifica sustituir el clásico; KEEP_CLASSIC.")
else:
    print("La mejora es pequeña; CONTINUE_EXPERIMENT.")

# Exportación para P06
artifact_candidates = [
    Path("../enterprise-genai-assistant/artifacts"),
    Path("M03/enterprise-genai-assistant/artifacts"),
]
artifact_dir = artifact_candidates[0]
if not artifact_dir.parent.exists() and artifact_candidates[1].parent.exists():
    artifact_dir = artifact_candidates[1]

artifact_dir.mkdir(parents=True, exist_ok=True)

joblib.dump(classic_pipeline, artifact_dir / "classic_router.joblib")
joblib.dump(neural_preprocessor, artifact_dir / "neural_preprocessor.joblib")
joblib.dump(label_encoder, artifact_dir / "neural_label_encoder.joblib")
torch.save(model.state_dict(), artifact_dir / "neural_router.pt")

config = {
    "input_dim": int(Xtr.shape[1]),
    "hidden_dim": hidden_dim,
    "num_classes": int(len(label_encoder.classes_)),
    "model_version": "m03-neural-v1",
}
(artifact_dir / "neural_router_config.json").write_text(
    json.dumps(config, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print("artefactos:", artifact_dir.resolve())

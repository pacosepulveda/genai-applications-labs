import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

torch.manual_seed(42)
np.random.seed(42)

digits = load_digits()
X = digits.images.astype("float32") / 16.0
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

Xtr_mlp = torch.tensor(X_train.reshape(len(X_train), -1), dtype=torch.float32)
Xte_mlp = torch.tensor(X_test.reshape(len(X_test), -1), dtype=torch.float32)
Xtr_cnn = torch.tensor(X_train[:, None, :, :], dtype=torch.float32)
Xte_cnn = torch.tensor(X_test[:, None, :, :], dtype=torch.float32)
ytr = torch.tensor(y_train, dtype=torch.long)


class SmallMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 10),
        )

    def forward(self, x):
        return self.net(x)


class SmallCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 8, kernel_size=3, padding=1)
        self.features = nn.Sequential(
            self.conv1,
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(8, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.classifier = nn.Linear(16 * 2 * 2, 10)

    def forward(self, x):
        x = self.features(x)
        x = x.flatten(1)
        return self.classifier(x)


def fit_model(model, Xtrain, ytrain, epochs=10, batch_size=64):
    loader = DataLoader(
        TensorDataset(Xtrain, ytrain),
        batch_size=batch_size,
        shuffle=True,
    )
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)

    for _ in range(epochs):
        model.train()
        for xb, yb in loader:
            optimizer.zero_grad()
            loss = loss_fn(model(xb), yb)
            loss.backward()
            optimizer.step()


def predict(model, X):
    model.eval()
    with torch.no_grad():
        return model(X).argmax(1).cpu().numpy()


mlp = SmallMLP()
cnn = SmallCNN()

fit_model(mlp, Xtr_mlp, ytr, epochs=10)
fit_model(cnn, Xtr_cnn, ytr, epochs=10)

mlp_pred = predict(mlp, Xte_mlp)
cnn_pred = predict(cnn, Xte_cnn)

print("MLP accuracy:", accuracy_score(y_test, mlp_pred))
print("CNN accuracy:", accuracy_score(y_test, cnn_pred))
print("MLP parámetros:", sum(p.numel() for p in mlp.parameters()))
print("CNN parámetros:", sum(p.numel() for p in cnn.parameters()))

sample = Xte_cnn[0:1]
with torch.no_grad():
    maps = cnn.conv1(sample)[0].cpu().numpy()

fig, axes = plt.subplots(2, 4, figsize=(8, 4))
for i, ax in enumerate(axes.ravel()):
    ax.imshow(maps[i], cmap="gray")
    ax.set_title(f"canal {i}")
    ax.axis("off")
plt.tight_layout()
plt.show()

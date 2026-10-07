import math
import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

torch.manual_seed(42)
np.random.seed(42)

# Parte A — scaled dot-product attention
Q = torch.tensor([
    [1.0, 0.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 1.0],
    [1.0, 1.0, 0.0, 0.0],
])
K = Q.clone()
V = torch.tensor([
    [1.0, 0.0],
    [0.0, 1.0],
    [1.0, 1.0],
])

d_k = Q.shape[-1]
scores = Q @ K.T / math.sqrt(d_k)
weights = torch.softmax(scores, dim=-1)
output = weights @ V

print("scores:\n", scores)
print("weights:\n", weights)
print("suma por fila:", weights.sum(dim=-1))
print("output:\n", output)

# Parte B — causal mask
seq_len = Q.shape[0]
future_mask = torch.triu(
    torch.ones(seq_len, seq_len, dtype=torch.bool),
    diagonal=1,
)
masked_scores = scores.masked_fill(future_mask, float("-inf"))
causal_weights = torch.softmax(masked_scores, dim=-1)
causal_output = causal_weights @ V

print("\ncausal mask:\n", future_mask)
print("causal weights:\n", causal_weights)
print("suma por fila:", causal_weights.sum(dim=-1))
print("causal output:\n", causal_output)

# Parte C — multi-head attention
mha = nn.MultiheadAttention(
    embed_dim=8,
    num_heads=2,
    batch_first=True,
)
x = torch.randn(2, 5, 8)
out, attn_weights = mha(x, x, x, need_weights=True)

print("\nMHA input:", x.shape)
print("MHA output:", out.shape)
print("MHA attention weights:", attn_weights.shape)

# Parte D — mini Transformer completo
def make_dataset(n=2000, seq_len=12, vocab_size=20, seed=42):
    rng = np.random.default_rng(seed)
    X = rng.integers(1, vocab_size, size=(n, seq_len))
    y = np.zeros(n, dtype=np.int64)

    half = n // 2
    y[:half] = 1
    X[:half, -1] = X[:half, 0]

    for i in range(half, n):
        if X[i, -1] == X[i, 0]:
            X[i, -1] = (X[i, 0] % (vocab_size - 1)) + 1

    order = rng.permutation(n)
    return X[order], y[order]


X, y = make_dataset()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

train_loader = DataLoader(
    TensorDataset(
        torch.tensor(X_train, dtype=torch.long),
        torch.tensor(y_train, dtype=torch.long),
    ),
    batch_size=64,
    shuffle=True,
)


class TinyTransformer(nn.Module):
    def __init__(self, vocab_size=21, d_model=32, nhead=4, seq_len=12):
        super().__init__()
        self.token_embedding = nn.Embedding(vocab_size, d_model)
        self.position_embedding = nn.Embedding(seq_len, d_model)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=64,
            batch_first=True,
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=1)
        self.classifier = nn.Linear(d_model * 2, 2)

    def forward(self, x):
        batch, seq_len = x.shape
        positions = torch.arange(seq_len, device=x.device).unsqueeze(0).expand(batch, -1)
        h = self.token_embedding(x) + self.position_embedding(positions)
        h = self.encoder(h)
        endpoints = torch.cat([h[:, 0, :], h[:, -1, :]], dim=-1)
        return self.classifier(endpoints)


model = TinyTransformer()
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=2e-3)

for epoch in range(1, 11):
    model.train()
    for xb, yb in train_loader:
        optimizer.zero_grad()
        loss = loss_fn(model(xb), yb)
        loss.backward()
        optimizer.step()

model.eval()
with torch.no_grad():
    pred = model(torch.tensor(X_test, dtype=torch.long)).argmax(1).numpy()

print("Transformer accuracy:", accuracy_score(y_test, pred))

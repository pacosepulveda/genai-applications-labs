import numpy as np
import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

torch.manual_seed(42)
np.random.seed(42)

digits = load_digits()
X = digits.images.astype("float32") / 16.0
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
train_tensor = torch.from_numpy(X_train.reshape(-1, 64))
test_tensor = torch.from_numpy(X_test.reshape(-1, 64))
loader = DataLoader(TensorDataset(train_tensor), batch_size=64, shuffle=True, num_workers=0)

class VAE(nn.Module):
    def __init__(self, latent_dim=2):
        super().__init__()
        self.encoder = nn.Sequential(nn.Linear(64, 32), nn.ReLU())
        self.mu = nn.Linear(32, latent_dim)
        self.log_var = nn.Linear(32, latent_dim)
        self.decoder = nn.Sequential(nn.Linear(latent_dim, 32), nn.ReLU(), nn.Linear(32, 64), nn.Sigmoid())

    def reparameterize(self, mu, log_var):
        sigma = torch.exp(0.5 * log_var)
        epsilon = torch.randn_like(sigma)
        return mu + sigma * epsilon

    def encode(self, x):
        h = self.encoder(x)
        return self.mu(h), self.log_var(h)

    def decode(self, z):
        return self.decoder(z)

    def forward(self, x):
        mu, log_var = self.encode(x)
        z = self.reparameterize(mu, log_var)
        return self.decode(z), mu, log_var

def vae_loss(recon, x, mu, log_var, beta=1.0):
    recon_loss = nn.functional.binary_cross_entropy(recon, x, reduction="sum") / x.shape[0]
    kl_loss = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp()) / x.shape[0]
    return recon_loss + beta * kl_loss, recon_loss, kl_loss

model = VAE(latent_dim=2)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
history = []
epochs = 25

for epoch in range(1, epochs + 1):
    model.train()
    total_sum = recon_sum = kl_sum = 0.0
    batches = 0
    for (xb,) in loader:
        optimizer.zero_grad()
        recon, mu, log_var = model(xb)
        loss, rec, kl = vae_loss(recon, xb, mu, log_var)
        loss.backward()
        optimizer.step()
        total_sum += loss.item(); recon_sum += rec.item(); kl_sum += kl.item(); batches += 1
    row = {"epoch": epoch, "total": total_sum / batches, "reconstruction": recon_sum / batches, "kl": kl_sum / batches}
    history.append(row)
    if epoch == 1 or epoch % 5 == 0:
        print(row)

plt.figure(figsize=(7,4))
plt.plot([r["epoch"] for r in history], [r["total"] for r in history], label="total")
plt.plot([r["epoch"] for r in history], [r["reconstruction"] for r in history], label="reconstruction")
plt.plot([r["epoch"] for r in history], [r["kl"] for r in history], label="KL")
plt.legend(); plt.title("VAE training"); plt.show()

model.eval()
with torch.no_grad():
    examples = test_tensor[:8]
    recon, _, _ = model(examples)
fig, axes = plt.subplots(2, 8, figsize=(12, 3))
for i in range(8):
    axes[0, i].imshow(examples[i].reshape(8, 8), cmap="gray", vmin=0, vmax=1)
    axes[1, i].imshow(recon[i].reshape(8, 8), cmap="gray", vmin=0, vmax=1)
    axes[0, i].axis("off"); axes[1, i].axis("off")
plt.tight_layout(); plt.show()

with torch.no_grad():
    z = torch.randn(16, 2)
    samples = model.decode(z).reshape(-1, 8, 8)
fig, axes = plt.subplots(4, 4, figsize=(5, 5))
for ax, image in zip(axes.ravel(), samples):
    ax.imshow(image, cmap="gray", vmin=0, vmax=1); ax.axis("off")
plt.tight_layout(); plt.show()

with torch.no_grad():
    mu_test, _ = model.encode(test_tensor)
mu_np = mu_test.numpy()
plt.figure(figsize=(6,5))
scatter = plt.scatter(mu_np[:,0], mu_np[:,1], c=y_test, s=18)
plt.colorbar(scatter, label="clase"); plt.show()

idx_a = 0
idx_b = next(i for i in range(1, len(y_test)) if y_test[i] != y_test[idx_a])
with torch.no_grad():
    mu_a, _ = model.encode(test_tensor[idx_a:idx_a+1])
    mu_b, _ = model.encode(test_tensor[idx_b:idx_b+1])
    alphas = torch.linspace(0, 1, 10).unsqueeze(1)
    interp = model.decode((1-alphas)*mu_a + alphas*mu_b).reshape(-1,8,8)
fig, axes = plt.subplots(1,10,figsize=(12,2))
for ax,image in zip(axes, interp):
    ax.imshow(image,cmap="gray",vmin=0,vmax=1); ax.axis("off")
plt.tight_layout(); plt.show()

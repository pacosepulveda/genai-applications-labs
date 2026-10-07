import json
from pathlib import Path
import numpy as np
import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

def find_m04_root():
    cwd = Path.cwd()
    for candidate in [cwd, cwd.parent, cwd / "M04"]:
        if (candidate / "enterprise-genai-assistant").exists():
            return candidate
    raise RuntimeError("No encuentro M04/enterprise-genai-assistant")

torch.manual_seed(42)
np.random.seed(42)

digits = load_digits()
X = digits.images.astype("float32") / 16.0
X = X * 2.0 - 1.0
tensor = torch.from_numpy(X[:, None, :, :])
loader = DataLoader(TensorDataset(tensor), batch_size=64, shuffle=True, num_workers=0)

LATENT_DIM = 32
HIDDEN_DIM = 128

class Generator(nn.Module):
    def __init__(self, latent_dim=LATENT_DIM, hidden_dim=HIDDEN_DIM):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim), nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim), nn.ReLU(),
            nn.Linear(hidden_dim, 64), nn.Tanh(),
        )
    def forward(self, z):
        return self.net(z).reshape(-1, 1, 8, 8)

class Discriminator(nn.Module):
    def __init__(self, hidden_dim=HIDDEN_DIM):
        super().__init__()
        self.net = nn.Sequential(
            nn.Flatten(), nn.Linear(64, hidden_dim), nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim, hidden_dim // 2), nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim // 2, 1),
        )
    def forward(self, x):
        return self.net(x).squeeze(1)

G = Generator()
D = Discriminator()
loss_fn = nn.BCEWithLogitsLoss()
opt_g = torch.optim.Adam(G.parameters(), lr=2e-4, betas=(0.5, 0.999))
opt_d = torch.optim.Adam(D.parameters(), lr=2e-4, betas=(0.5, 0.999))
fixed_noise = torch.randn(16, LATENT_DIM)
history, snapshots = [], {}
epochs = 30

for epoch in range(1, epochs + 1):
    g_sum = d_sum = 0.0
    batches = 0
    for (real,) in loader:
        batch_size = real.shape[0]
        z = torch.randn(batch_size, LATENT_DIM)
        fake = G(z)

        opt_d.zero_grad()
        real_logits = D(real)
        fake_logits = D(fake.detach())
        d_loss = loss_fn(real_logits, torch.ones_like(real_logits)) + loss_fn(fake_logits, torch.zeros_like(fake_logits))
        d_loss.backward()
        opt_d.step()

        z = torch.randn(batch_size, LATENT_DIM)
        opt_g.zero_grad()
        generated = G(z)
        logits = D(generated)
        g_loss = loss_fn(logits, torch.ones_like(logits))
        g_loss.backward()
        opt_g.step()

        d_sum += d_loss.item(); g_sum += g_loss.item(); batches += 1

    history.append({"epoch": epoch, "d_loss": d_sum / batches, "g_loss": g_sum / batches})
    if epoch in {1, 5, 10, 20, 30}:
        G.eval()
        with torch.no_grad():
            snapshots[epoch] = G(fixed_noise).cpu().clone()
        G.train()
    if epoch == 1 or epoch % 5 == 0:
        print(history[-1])

plt.figure(figsize=(7,4))
plt.plot([r["epoch"] for r in history], [r["d_loss"] for r in history], label="D")
plt.plot([r["epoch"] for r in history], [r["g_loss"] for r in history], label="G")
plt.legend(); plt.title("GAN losses"); plt.show()

for epoch, images in snapshots.items():
    images = ((images + 1) / 2).clamp(0, 1)
    fig, axes = plt.subplots(4, 4, figsize=(4, 4))
    for ax, image in zip(axes.ravel(), images):
        ax.imshow(image.squeeze(0), cmap="gray", vmin=0, vmax=1); ax.axis("off")
    plt.suptitle(f"fixed noise — epoch {epoch}"); plt.tight_layout(); plt.show()

ART = find_m04_root() / "enterprise-genai-assistant" / "artifacts"
ART.mkdir(parents=True, exist_ok=True)
config = {"latent_dim": LATENT_DIM, "hidden_dim": HIDDEN_DIM, "image_size": 8, "channels": 1, "model_version": "m04-p03"}
torch.save(G.state_dict(), ART / "generator.pt")
(ART / "gan_config.json").write_text(json.dumps(config, indent=2), encoding="utf-8")
torch.save({
    "generator_state_dict": G.state_dict(),
    "discriminator_state_dict": D.state_dict(),
    "optimizer_g_state_dict": opt_g.state_dict(),
    "optimizer_d_state_dict": opt_d.state_dict(),
    "epoch": epochs,
    "config": config,
}, ART / "gan_checkpoint.pt")
print("artefactos guardados en:", ART.resolve())

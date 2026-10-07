import numpy as np
import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

torch.manual_seed(42)
np.random.seed(42)

digits = load_digits()
X = digits.images.astype("float32") / 16.0
X = X * 2.0 - 1.0
X = torch.from_numpy(X.reshape(-1, 64))
loader = DataLoader(TensorDataset(X), batch_size=64, shuffle=True, num_workers=0)

T = 40
betas = torch.linspace(1e-4, 0.08, T)
alphas = 1.0 - betas
alpha_bars = torch.cumprod(alphas, dim=0)

def q_sample(x0, t, noise=None):
    if noise is None:
        noise = torch.randn_like(x0)
    alpha_bar_t = alpha_bars[t].unsqueeze(1)
    xt = torch.sqrt(alpha_bar_t) * x0 + torch.sqrt(1.0 - alpha_bar_t) * noise
    return xt, noise

x0 = X[0:1]
steps = [0, 5, 15, 25, 39]
fig, axes = plt.subplots(1, len(steps), figsize=(9, 2))
for ax, t_index in zip(axes, steps):
    xt, _ = q_sample(x0, torch.tensor([t_index], dtype=torch.long), noise=torch.randn_like(x0))
    ax.imshow(xt[0].reshape(8, 8), cmap="gray", vmin=-1, vmax=1)
    ax.set_title(f"t={t_index}")
    ax.axis("off")
plt.tight_layout(); plt.show()

def timestep_features(t, T):
    return t.float().unsqueeze(1) / float(T - 1)

class TinyDenoiser(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(65, 128), nn.ReLU(),
            nn.Linear(128, 128), nn.ReLU(),
            nn.Linear(128, 64),
        )
    def forward(self, x, t):
        return self.net(torch.cat([x, timestep_features(t, T)], dim=1))

model = TinyDenoiser()
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()
history = []
epochs = 18

for epoch in range(1, epochs + 1):
    model.train()
    epoch_loss = 0.0
    batches = 0
    for (x0_batch,) in loader:
        batch_size = x0_batch.shape[0]
        t = torch.randint(0, T, (batch_size,), dtype=torch.long)
        epsilon = torch.randn_like(x0_batch)
        xt, _ = q_sample(x0_batch, t, epsilon)
        optimizer.zero_grad()
        pred_noise = model(xt, t)
        loss = loss_fn(pred_noise, epsilon)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item(); batches += 1
    avg = epoch_loss / batches
    history.append(avg)
    if epoch == 1 or epoch % 3 == 0:
        print("epoch", epoch, "loss", round(avg, 5))

plt.figure(figsize=(7, 4))
plt.plot(range(1, epochs + 1), history)
plt.xlabel("epoch"); plt.ylabel("MSE"); plt.title("Tiny diffusion — predicción de ruido"); plt.show()

@torch.no_grad()
def p_sample_step(model, x_t, t_index):
    batch_size = x_t.shape[0]
    t = torch.full((batch_size,), t_index, dtype=torch.long)
    epsilon_pred = model(x_t, t)
    beta_t = betas[t_index]
    alpha_t = alphas[t_index]
    alpha_bar_t = alpha_bars[t_index]
    mean = (1.0 / torch.sqrt(alpha_t)) * (
        x_t - beta_t / torch.sqrt(1.0 - alpha_bar_t) * epsilon_pred
    )
    if t_index > 0:
        return mean + torch.sqrt(beta_t) * torch.randn_like(x_t)
    return mean

model.eval()
samples = torch.randn(16, 64)
snapshots = {}
for t_index in reversed(range(T)):
    samples = p_sample_step(model, samples, t_index)
    if t_index in {39, 30, 20, 10, 0}:
        snapshots[t_index] = samples.clone()

for t_index in [39, 30, 20, 10, 0]:
    images = snapshots[t_index].reshape(-1, 8, 8).clamp(-1, 1)
    fig, axes = plt.subplots(4, 4, figsize=(4, 4))
    for ax, image in zip(axes.ravel(), images):
        ax.imshow(image, cmap="gray", vmin=-1, vmax=1)
        ax.axis("off")
    plt.suptitle(f"reverse sampling — t={t_index}")
    plt.tight_layout(); plt.show()

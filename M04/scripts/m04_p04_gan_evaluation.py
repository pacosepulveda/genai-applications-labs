import json
from pathlib import Path
import numpy as np
import torch
from torch import nn
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, pairwise_distances
import matplotlib.pyplot as plt

def find_m04_root():
    cwd = Path.cwd()
    for candidate in [cwd, cwd.parent, cwd / "M04"]:
        if (candidate / "enterprise-genai-assistant").exists():
            return candidate
    raise RuntimeError("No encuentro M04/enterprise-genai-assistant")

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

ART = find_m04_root() / "enterprise-genai-assistant" / "artifacts"
if not (ART / "generator.pt").exists():
    raise RuntimeError("P04 necesita el generator entrenado. Ejecuta primero M04.P03.")

config = json.loads((ART / "gan_config.json").read_text(encoding="utf-8"))
G = Generator(int(config["latent_dim"]), int(config["hidden_dim"]))
G.load_state_dict(torch.load(ART / "generator.pt", map_location="cpu", weights_only=True))
G.eval()

torch.manual_seed(123)
with torch.no_grad():
    generated_t = G(torch.randn(500, int(config["latent_dim"])))
generated = ((generated_t + 1.0) / 2.0).clamp(0, 1)
generated_np = generated.squeeze(1).numpy()

fig, axes = plt.subplots(4, 8, figsize=(8, 4))
for ax, image in zip(axes.ravel(), generated_np[:32]):
    ax.imshow(image, cmap="gray", vmin=0, vmax=1)
    ax.axis("off")
plt.tight_layout(); plt.show()

pixel_std_mean = float(generated_np.std(axis=0).mean())
flat = generated_np.reshape(len(generated_np), -1)
distances = pairwise_distances(flat[:150], metric="euclidean")
upper = distances[np.triu_indices_from(distances, k=1)]
mean_pair_distance = float(upper.mean())
near_duplicate_ratio = float((upper < 0.35).mean())
print("std medio por píxel:", pixel_std_mean)
print("distancia media entre pares:", mean_pair_distance)
print("ratio de pares casi duplicados:", near_duplicate_ratio)

digits = load_digits()
X_real = digits.images.astype("float32") / 16.0
y_real = digits.target
X_train, X_test, y_train, y_test = train_test_split(
    X_real.reshape(-1,64), y_real, test_size=0.20, random_state=42, stratify=y_real
)
clf = LogisticRegression(max_iter=1500).fit(X_train, y_train)
print("accuracy sonda sobre test real:", accuracy_score(y_test, clf.predict(X_test)))
synthetic_pred = clf.predict(flat)
classes, counts = np.unique(synthetic_pred, return_counts=True)
distribution = {int(c): int(n) for c, n in zip(classes, counts)}
print("distribución predicha sobre sintéticos:", distribution)
top_class_share = float((counts / counts.sum()).max())

suspected_collapse = (
    pixel_std_mean < 0.08
    or top_class_share > 0.45
    or near_duplicate_ratio > 0.10
)
print("share de la clase más frecuente:", top_class_share)
print("sospecha de mode collapse:", suspected_collapse)

plt.figure(figsize=(7, 3))
plt.bar(classes.astype(str), counts)
plt.xlabel("clase predicha por la sonda")
plt.ylabel("número de imágenes")
plt.title("Cobertura aproximada de la GAN")
plt.show()

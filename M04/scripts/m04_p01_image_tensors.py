import numpy as np
import torch
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from torch.utils.data import TensorDataset, DataLoader

digits = load_digits()
X = digits.images
y = digits.target

print("shape:", X.shape)
print("dtype:", X.dtype)
print("range:", X.min(), X.max())
print("classes:", np.unique(y))

img = X[0]
t2 = torch.tensor(img, dtype=torch.float32)
t3 = t2.unsqueeze(0)
batch = torch.tensor(X[:32], dtype=torch.float32).unsqueeze(1)
print("t2:", t2.shape)
print("t3:", t3.shape)
print("batch:", batch.shape)

img_01 = img.astype("float32") / 16.0
img_m11 = img_01 * 2.0 - 1.0
print("[0,1]:", img_01.min(), img_01.max())
print("[-1,1]:", img_m11.min(), img_m11.max())

rng = np.random.default_rng(42)

def add_noise(image, sigma=0.08):
    noisy = image + rng.normal(0.0, sigma, size=image.shape)
    return np.clip(noisy, 0.0, 1.0)

def shift_right(image, pixels=1):
    shifted = np.zeros_like(image)
    shifted[:, pixels:] = image[:, :-pixels]
    return shifted

def reduce_intensity(image, factor=0.8):
    return np.clip(image * factor, 0.0, 1.0)

original = X[0].astype("float32") / 16.0
augmented = [
    ("original", original),
    ("noise", add_noise(original)),
    ("shift", shift_right(original, 1)),
    ("intensity", reduce_intensity(original)),
]

fig, axes = plt.subplots(1, len(augmented), figsize=(8, 2))
for ax, (name, image) in zip(axes, augmented):
    ax.imshow(image, cmap="gray", vmin=0, vmax=1)
    ax.set_title(name)
    ax.axis("off")
plt.tight_layout()
plt.show()

bad = original.copy()
bad[:, :4] = 0.0
plt.figure(figsize=(2, 2))
plt.imshow(bad, cmap="gray", vmin=0, vmax=1)
plt.title("transformación problemática")
plt.axis("off")
plt.show()

X_m11 = (X.astype("float32") / 16.0) * 2.0 - 1.0
all_images = torch.from_numpy(X_m11[:, None, :, :])
all_labels = torch.from_numpy(y.astype("int64"))
dataset = TensorDataset(all_images, all_labels)
loader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=0)
xb, yb = next(iter(loader))
print("batch images:", xb.shape)
print("batch labels:", yb.shape)
print("batch range:", xb.min().item(), xb.max().item())

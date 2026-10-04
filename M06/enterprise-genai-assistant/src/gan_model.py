import torch
from torch import nn


class Generator(nn.Module):
    def __init__(self, latent_dim: int = 32, hidden_dim: int = 128):
        super().__init__()
        self.latent_dim = latent_dim
        self.net = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 64),
            nn.Tanh(),
        )

    def forward(self, z):
        return self.net(z).view(-1, 1, 8, 8)

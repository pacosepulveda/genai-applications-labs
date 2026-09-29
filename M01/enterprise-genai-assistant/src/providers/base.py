from dataclasses import dataclass
from typing import Protocol

@dataclass
class GenerationResult:
    text: str
    provider: str
    model: str

class Provider(Protocol):
    def generate(self, prompt: str) -> GenerationResult: ...

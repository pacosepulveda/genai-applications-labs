from pathlib import Path
import json
from PIL import Image

class ArtifactStore:
    def __init__(self, root: str | Path):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def save(self, artifact_id: str, image: Image.Image, metadata: dict):
        image_path = self.root / f"{artifact_id}.png"
        metadata_path = self.root / f"{artifact_id}.json"

        image.save(image_path)
        metadata_path.write_text(
            json.dumps(metadata, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        return image_path, metadata_path

    def load_metadata(self, artifact_id: str) -> dict:
        path = self.root / f"{artifact_id}.json"
        return json.loads(path.read_text(encoding="utf-8"))

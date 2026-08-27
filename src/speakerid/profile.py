from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass
class VoiceProfile:
    """A stored voice profile."""

    name: str
    embeddings: list[np.ndarray]
    path: Path | None = None

    def __post_init__(self) -> None:
        if self.path is not None:
            self.path = Path(self.path)

    @property
    def embedding(self) -> np.ndarray:
        """Return the average embedding of the profile."""

        if not self.embeddings:
            raise ValueError("Profile contains no embeddings")

        embedding = np.mean(
            np.stack(self.embeddings),
            axis=0,
        )

        norm = np.linalg.norm(embedding)

        if norm == 0:
            raise ValueError("Profile embedding is a zero vector")

        return (embedding / norm).astype(np.float32)
from pathlib import Path

import numpy as np

from .profile import VoiceProfile


def save(
    profile: VoiceProfile,
    output: str | Path | None = None,
) -> Path:
    """Save a voice profile to disk."""

    if not isinstance(profile, VoiceProfile):
        raise TypeError("profile must be a VoiceProfile")

    if not profile.name.strip():
        raise ValueError("profile name cannot be empty")

    if not profile.embeddings:
        raise ValueError("profile contains no embeddings")

    if output is None:
        if profile.path is None:
            raise ValueError(
                "output is required when profile.path is not set"
            )

        output = Path(profile.path) / "profile.npz"

    output = Path(output)

    if output.suffix != ".npz":
        output = output.with_suffix(".npz")

    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    embeddings = np.stack(profile.embeddings).astype(
        np.float32
    )

    np.savez_compressed(
        output,
        name=profile.name,
        embeddings=embeddings,
    )

    return output


def load(
    path: str | Path,
) -> VoiceProfile:
    """Load a voice profile from disk."""

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(
            f"Profile not found: {path}"
        )

    if not path.is_file():
        raise ValueError(
            f"Profile path is not a file: {path}"
        )

    if path.suffix != ".npz":
        raise ValueError(
            "Profile file must use the .npz format"
        )

    try:
        with np.load(path, allow_pickle=False) as data:
            name = str(data["name"].item())
            embeddings = data["embeddings"].astype(
                np.float32
            )

    except (KeyError, ValueError, OSError) as exc:
        raise ValueError(
            f"Invalid profile file: {path}"
        ) from exc

    if embeddings.ndim != 2:
        raise ValueError(
            "Profile embeddings must be a 2D array"
        )

    if embeddings.shape[0] == 0:
        raise ValueError(
            "Profile contains no embeddings"
        )

    return VoiceProfile(
        name=name,
        embeddings=[
            embedding.copy()
            for embedding in embeddings
        ],
        path=path.parent,
    )
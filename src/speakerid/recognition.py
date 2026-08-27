import numpy as np


def compare(
    first: np.ndarray,
    second: np.ndarray,
) -> float:
    """Compare two speaker embeddings using cosine similarity."""

    first = np.asarray(first, dtype=np.float32)
    second = np.asarray(second, dtype=np.float32)

    if first.ndim != 1 or second.ndim != 1:
        raise ValueError("Embeddings must be one-dimensional")

    if first.shape != second.shape:
        raise ValueError("Embeddings must have the same shape")

    first_norm = np.linalg.norm(first)
    second_norm = np.linalg.norm(second)

    if first_norm == 0 or second_norm == 0:
        raise ValueError("Embeddings must not be zero vectors")

    return float(
        np.dot(first, second)
        / (first_norm * second_norm)
    )

def verify(
    first: np.ndarray,
    second: np.ndarray,
    threshold: float = 0.75,
) -> bool:
    """Verify whether two speaker embeddings belong to the same person."""

    if not 0.0 <= threshold <= 1.0:
        raise ValueError("threshold must be between 0 and 1")

    score = compare(first, second)

    return score >= threshold

def identify(
    embedding: np.ndarray,
    profiles: dict[str, np.ndarray],
    threshold: float = 0.75,
) -> tuple[str | None, float]:
    """Identify the person closest to a speaker embedding."""

    if not 0.0 <= threshold <= 1.0:
        raise ValueError("threshold must be between 0 and 1")

    if not profiles:
        return None, 0.0

    best_name: str | None = None
    best_score = -1.0

    for name, profile in profiles.items():
        score = compare(embedding, profile)

        if score > best_score:
            best_score = score
            best_name = name

    if best_score < threshold:
        return None, best_score

    return best_name, best_score
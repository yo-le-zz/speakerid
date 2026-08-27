from pathlib import Path


def record(
    output: str | Path | None = None,
    duration: float = 5.0,
    sample_rate: int = 16000,
    channels: int = 1,
    device: int | str | None = None,
    phrase: str | None = None,
) -> Path:
    """Record audio from a microphone."""
    raise NotImplementedError
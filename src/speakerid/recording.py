from datetime import datetime
from pathlib import Path

import sounddevice as sd
import soundfile as sf


def record(
    output: str | Path | None = None,
    duration: float = 5.0,
    sample_rate: int = 16000,
    channels: int = 1,
    device: int | str | None = None,
) -> Path:
    """Record audio from a microphone."""

    if duration <= 0:
        raise ValueError("duration must be greater than 0")

    if sample_rate <= 0:
        raise ValueError("sample_rate must be greater than 0")

    if channels <= 0:
        raise ValueError("channels must be greater than 0")

    if output is None:
        output = Path(
            "records"
            f"/record_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        )
    else:
        output = Path(output)

    output.parent.mkdir(parents=True, exist_ok=True)

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=channels,
        device=device,
        dtype="float32",
    )

    sd.wait()

    sf.write(
        output,
        audio,
        sample_rate,
        subtype="PCM_16",
    )

    return output
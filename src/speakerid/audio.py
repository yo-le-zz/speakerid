from pathlib import Path

import librosa
import noisereduce as nr
import numpy as np
import soundfile as sf


def clean(
    input: str | Path,
    output: str | Path | None = None,
    noise_reduction: bool = True,
    normalize: bool = True,
    remove_silence: bool = True,
    highpass: bool = True,
) -> Path:
    """Clean and process an audio file."""

    input = Path(input)

    if not input.exists():
        raise FileNotFoundError(f"Audio file not found: {input}")

    if not input.is_file():
        raise ValueError(f"Input is not a file: {input}")

    if output is None:
        output = input.with_name(f"{input.stem}_clean.wav")
    else:
        output = Path(output)

    output.parent.mkdir(parents=True, exist_ok=True)

    audio, sample_rate = librosa.load(
        input,
        sr=None,
        mono=True,
    )

    if len(audio) == 0:
        raise ValueError("Audio file is empty")

    if highpass:
        audio = librosa.effects.preemphasis(audio)

    if noise_reduction:
        audio = nr.reduce_noise(
            y=audio,
            sr=sample_rate,
        )

    if remove_silence:
        intervals = librosa.effects.split(
            audio,
            top_db=30,
        )

        if len(intervals) > 0:
            audio = np.concatenate(
                [audio[start:end] for start, end in intervals]
            )

    if normalize:
        peak = np.max(np.abs(audio))

        if peak > 0:
            audio = audio / peak

    sf.write(
        output,
        audio,
        sample_rate,
        subtype="PCM_16",
    )

    return output
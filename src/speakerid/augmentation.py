from pathlib import Path

import librosa
import numpy as np
import soundfile as sf


def augment(
    input: str | Path,
    output_dir: str | Path,
    count: int = 5,
    noise: bool = True,
    reverb: bool = True,
    speed: bool = True,
    pitch: bool = True,
    volume: bool = True,
) -> list[Path]:
    """Generate augmented audio variations."""

    input = Path(input)
    output_dir = Path(output_dir)

    if not input.exists():
        raise FileNotFoundError(f"Audio file not found: {input}")

    if not input.is_file():
        raise ValueError(f"Input is not a file: {input}")

    if count <= 0:
        raise ValueError("count must be greater than 0")

    if not any((noise, reverb, speed, pitch, volume)):
        raise ValueError("At least one augmentation must be enabled")

    output_dir.mkdir(parents=True, exist_ok=True)

    audio, sample_rate = librosa.load(
        input,
        sr=None,
        mono=True,
    )

    if len(audio) == 0:
        raise ValueError("Audio file is empty")

    results: list[Path] = []

    for index in range(1, count + 1):
        augmented = audio.copy()

        if noise:
            noise_level = np.random.uniform(0.001, 0.01)

            noise_data = np.random.normal(
                0,
                noise_level,
                size=augmented.shape,
            )

            augmented += noise_data

        if speed:
            rate = np.random.uniform(0.9, 1.1)

            augmented = librosa.effects.time_stretch(
                augmented,
                rate=rate,
            )

        if pitch:
            steps = np.random.uniform(-1.0, 1.0)

            augmented = librosa.effects.pitch_shift(
                augmented,
                sr=sample_rate,
                n_steps=steps,
            )

        if volume:
            gain = np.random.uniform(0.7, 1.3)
            augmented *= gain

        if reverb:
            delay = int(
                sample_rate * np.random.uniform(0.02, 0.05)
            )

            if delay < len(augmented):
                echo = np.zeros_like(augmented)

                echo[delay:] = (
                    augmented[:-delay]
                    * np.random.uniform(0.1, 0.3)
                )

                augmented += echo

        # Remove NaN and infinite values.
        augmented = np.nan_to_num(
            augmented,
            nan=0.0,
            posinf=1.0,
            neginf=-1.0,
        )

        # Prevent clipping.
        peak = np.max(np.abs(augmented))

        if peak > 1:
            augmented /= peak

        output = output_dir / (
            f"{input.stem}_aug_{index:02d}.wav"
        )

        sf.write(
            output,
            augmented,
            sample_rate,
            subtype="PCM_16",
        )

        results.append(output)

    return results
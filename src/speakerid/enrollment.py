from pathlib import Path

from .augmentation import augment as augment_audio
from .audio import clean as clean_audio
from .encoding import encode
from .profile import VoiceProfile
from .recording import record


def enroll(
    name: str,
    samples: int = 5,
    output_dir: str | Path = "voices",
    clean: bool = True,
    augment: bool = True,
    augmentation_count: int = 3,
    phrases: list[str] | None = None,
) -> VoiceProfile:
    """Create a voice profile for a person."""

    if not name.strip():
        raise ValueError("name cannot be empty")

    if samples <= 0:
        raise ValueError("samples must be greater than 0")

    if augmentation_count < 0:
        raise ValueError("augmentation_count cannot be negative")

    output_dir = Path(output_dir)
    person_dir = output_dir / name
    person_dir.mkdir(parents=True, exist_ok=True)

    embeddings = []

    for index in range(samples):
        audio = person_dir / f"sample_{index + 1:02d}.wav"

        phrase = None

        if phrases:
            phrase = phrases[index % len(phrases)]

        record(
            output=audio,
            duration=5.0,
            sample_rate=16000,
            channels=1,
            phrase=phrase,
        )

        source = audio

        if clean:
            cleaned = person_dir / f"sample_{index + 1:02d}_clean.wav"

            clean_audio(
                input=source,
                output=cleaned,
            )

            source = cleaned

        embeddings.append(
            encode(source)
        )

        if augment and augmentation_count > 0:
            augmented_dir = person_dir / "augmented"

            augmented_files = augment_audio(
                input=source,
                output_dir=augmented_dir,
                count=augmentation_count,
            )

            for augmented_file in augmented_files:
                embeddings.append(
                    encode(augmented_file)
                )

    return VoiceProfile(
        name=name,
        embeddings=embeddings,
        path=person_dir,
    )
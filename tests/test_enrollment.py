import numpy as np
import pytest

import speakerid.enrollment as enrollment


def test_enroll_invalid_name():
    with pytest.raises(ValueError):
        enrollment.enroll("")


def test_enroll_invalid_samples():
    with pytest.raises(ValueError):
        enrollment.enroll(
            "yolezz",
            samples=0,
        )


def test_enroll_invalid_augmentation_count():
    with pytest.raises(ValueError):
        enrollment.enroll(
            "yolezz",
            augmentation_count=-1,
        )


def test_enroll_creates_profile(monkeypatch, tmp_path):
    def fake_record(
        output,
        duration=5.0,
        sample_rate=16000,
        channels=1,
        device=None,
        phrase=None,
    ):
        output.parent.mkdir(
            parents=True,
            exist_ok=True,
        )
    
        output.write_bytes(b"fake audio")
    
        return output

    def fake_clean(
        input,
        output=None,
        **kwargs,
    ):
        output.write_bytes(b"fake cleaned audio")
        return output

    def fake_augment(
        input,
        output_dir,
        count=5,
        **kwargs,
    ):
        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        files = []

        for index in range(count):
            path = output_dir / f"aug_{index}.wav"
            path.write_bytes(b"fake augmented audio")
            files.append(path)

        return files

    def fake_encode(audio, sample_rate=16000):
        return np.ones(192, dtype=np.float32)

    monkeypatch.setattr(
        enrollment,
        "record",
        fake_record,
    )

    monkeypatch.setattr(
        enrollment,
        "clean_audio",
        fake_clean,
    )

    monkeypatch.setattr(
        enrollment,
        "augment_audio",
        fake_augment,
    )

    monkeypatch.setattr(
        enrollment,
        "encode",
        fake_encode,
    )

    profile = enrollment.enroll(
        name="yolezz",
        samples=2,
        output_dir=tmp_path,
        clean=True,
        augment=True,
        augmentation_count=2,
    )

    assert profile.name == "yolezz"
    assert profile.path == tmp_path / "yolezz"

    # 2 original samples + 2 augmentations per sample.
    assert len(profile.embeddings) == 6
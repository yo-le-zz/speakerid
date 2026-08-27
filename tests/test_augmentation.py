import numpy as np
import soundfile as sf

import speakerid


def create_test_audio(path, sample_rate=16000, duration=1.0):
    samples = int(sample_rate * duration)

    time = np.linspace(
        0,
        duration,
        samples,
        endpoint=False,
    )

    audio = 0.5 * np.sin(2 * np.pi * 440 * time)

    sf.write(
        path,
        audio,
        sample_rate,
    )


def test_augment_creates_files(tmp_path):
    input_file = tmp_path / "voice.wav"
    output_dir = tmp_path / "augmented"

    create_test_audio(input_file)

    results = speakerid.augment(
        input=input_file,
        output_dir=output_dir,
        count=5,
    )

    assert len(results) == 5

    for path in results:
        assert path.exists()
        assert path.is_file()


def test_augment_creates_valid_audio(tmp_path):
    input_file = tmp_path / "voice.wav"
    output_dir = tmp_path / "augmented"

    create_test_audio(input_file)

    results = speakerid.augment(
        input=input_file,
        output_dir=output_dir,
        count=3,
    )

    for path in results:
        audio, sample_rate = sf.read(path)

        assert len(audio) > 0
        assert sample_rate == 16000


def test_augment_custom_count(tmp_path):
    input_file = tmp_path / "voice.wav"
    output_dir = tmp_path / "augmented"

    create_test_audio(input_file)

    results = speakerid.augment(
        input=input_file,
        output_dir=output_dir,
        count=10,
    )

    assert len(results) == 10


def test_augment_missing_file(tmp_path):
    input_file = tmp_path / "missing.wav"
    output_dir = tmp_path / "augmented"

    try:
        speakerid.augment(
            input=input_file,
            output_dir=output_dir,
        )
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("Expected FileNotFoundError")


def test_augment_invalid_count(tmp_path):
    input_file = tmp_path / "voice.wav"
    output_dir = tmp_path / "augmented"

    create_test_audio(input_file)

    try:
        speakerid.augment(
            input=input_file,
            output_dir=output_dir,
            count=0,
        )
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")


def test_augment_all_disabled(tmp_path):
    input_file = tmp_path / "voice.wav"
    output_dir = tmp_path / "augmented"

    create_test_audio(input_file)

    try:
        speakerid.augment(
            input=input_file,
            output_dir=output_dir,
            noise=False,
            reverb=False,
            speed=False,
            pitch=False,
            volume=False,
        )
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")
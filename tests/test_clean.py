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


def test_clean_creates_file(tmp_path):
    input_file = tmp_path / "input.wav"
    output_file = tmp_path / "clean.wav"

    create_test_audio(input_file)

    result = speakerid.clean(
        input_file,
        output_file,
    )

    assert result == output_file
    assert output_file.exists()


def test_clean_default_output(tmp_path):
    input_file = tmp_path / "voice.wav"

    create_test_audio(input_file)

    result = speakerid.clean(input_file)

    expected = tmp_path / "voice_clean.wav"

    assert result == expected
    assert expected.exists()


def test_clean_output_is_valid_audio(tmp_path):
    input_file = tmp_path / "input.wav"
    output_file = tmp_path / "clean.wav"

    create_test_audio(input_file)

    speakerid.clean(
        input_file,
        output_file,
    )

    audio, sample_rate = sf.read(output_file)

    assert len(audio) > 0
    assert sample_rate == 16000


def test_clean_missing_file(tmp_path):
    input_file = tmp_path / "does_not_exist.wav"

    try:
        speakerid.clean(input_file)
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("Expected FileNotFoundError")


def test_clean_empty_file(tmp_path):
    input_file = tmp_path / "empty.wav"

    sf.write(
        input_file,
        np.array([], dtype=np.float32),
        16000,
    )

    try:
        speakerid.clean(input_file)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")
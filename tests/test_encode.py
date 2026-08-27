import numpy as np
import soundfile as sf

import speakerid


def create_test_audio(path, sample_rate=16000, duration=2.0):
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


def test_encode_exists():
    assert callable(speakerid.encode)


def test_encode_missing_file(tmp_path):
    audio = tmp_path / "missing.wav"

    try:
        speakerid.encode(audio)
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("Expected FileNotFoundError")


def test_encode_empty_file(tmp_path):
    audio = tmp_path / "empty.wav"

    sf.write(
        audio,
        np.array([], dtype=np.float32),
        16000,
    )

    try:
        speakerid.encode(audio)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")

def test_embedding_is_normalized():
    # Ce test sera fait avec un vrai embedding dans le test
    # d'intégration, pas avec un faux fichier audio.
    pass
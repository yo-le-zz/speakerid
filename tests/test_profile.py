import numpy as np
import pytest

from speakerid.profile import VoiceProfile


def test_profile_average_embedding():
    profile = VoiceProfile(
        name="yolezz",
        embeddings=[
            np.array([1.0, 0.0]),
            np.array([1.0, 0.0]),
        ],
    )

    embedding = profile.embedding

    assert embedding.shape == (2,)
    assert np.linalg.norm(embedding) == pytest.approx(1.0)
    assert embedding[0] == pytest.approx(1.0)
    assert embedding[1] == pytest.approx(0.0)


def test_profile_empty():
    profile = VoiceProfile(
        name="yolezz",
        embeddings=[],
    )

    with pytest.raises(ValueError):
        profile.embedding


def test_profile_path():
    profile = VoiceProfile(
        name="yolezz",
        embeddings=[],
        path="voices/yolezz",
    )

    assert profile.path.name == "yolezz"
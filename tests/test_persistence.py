import numpy as np
import pytest

import speakerid


def create_profile() -> speakerid.VoiceProfile:
    return speakerid.VoiceProfile(
        name="yolezz",
        embeddings=[
            np.array([1.0, 0.0, 0.0], dtype=np.float32),
            np.array([0.0, 1.0, 0.0], dtype=np.float32),
            np.array([0.0, 0.0, 1.0], dtype=np.float32),
        ],
    )


def test_save_creates_file(tmp_path):
    profile = create_profile()

    output = tmp_path / "profile.npz"

    result = speakerid.save(
        profile,
        output,
    )

    assert result == output
    assert output.exists()
    assert output.is_file()


def test_save_default_output(tmp_path):
    profile = create_profile()
    profile.path = tmp_path / "yolezz"

    result = speakerid.save(profile)

    assert result == tmp_path / "yolezz" / "profile.npz"
    assert result.exists()


def test_save_adds_extension(tmp_path):
    profile = create_profile()

    result = speakerid.save(
        profile,
        tmp_path / "profile",
    )

    assert result == tmp_path / "profile.npz"
    assert result.exists()


def test_save_invalid_profile():
    with pytest.raises(TypeError):
        speakerid.save("not a profile")


def test_save_empty_profile(tmp_path):
    profile = speakerid.VoiceProfile(
        name="yolezz",
        embeddings=[],
    )

    with pytest.raises(ValueError):
        speakerid.save(
            profile,
            tmp_path / "profile.npz",
        )


def test_save_without_output_or_path():
    profile = create_profile()

    with pytest.raises(ValueError):
        speakerid.save(profile)


def test_load_profile(tmp_path):
    original = create_profile()

    path = speakerid.save(
        original,
        tmp_path / "profile.npz",
    )

    loaded = speakerid.load(path)

    assert isinstance(
        loaded,
        speakerid.VoiceProfile,
    )

    assert loaded.name == "yolezz"
    assert len(loaded.embeddings) == 3

    for original_embedding, loaded_embedding in zip(
        original.embeddings,
        loaded.embeddings,
    ):
        np.testing.assert_array_equal(
            original_embedding,
            loaded_embedding,
        )


def test_load_preserves_path(tmp_path):
    profile = create_profile()

    path = speakerid.save(
        profile,
        tmp_path / "yolezz" / "profile.npz",
    )

    loaded = speakerid.load(path)

    assert loaded.path == tmp_path / "yolezz"


def test_load_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        speakerid.load(
            tmp_path / "does_not_exist.npz"
        )


def test_load_directory(tmp_path):
    directory = tmp_path / "profile"
    directory.mkdir()

    with pytest.raises(ValueError):
        speakerid.load(directory)


def test_load_wrong_extension(tmp_path):
    path = tmp_path / "profile.json"
    path.write_text("{}")

    with pytest.raises(ValueError):
        speakerid.load(path)


def test_load_invalid_file(tmp_path):
    path = tmp_path / "profile.npz"
    path.write_text("this is not a profile")

    with pytest.raises(ValueError):
        speakerid.load(path)
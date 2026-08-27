import numpy as np
import pytest

import speakerid


def test_identify_best_match():
    target = np.array([1.0, 0.0])

    profiles = {
        "yolezz": np.array([1.0, 0.0]),
        "alice": np.array([0.0, 1.0]),
        "bob": np.array([-1.0, 0.0]),
    }

    name, score = speakerid.identify(
        target,
        profiles,
        threshold=0.75,
    )

    assert name == "yolezz"
    assert score == pytest.approx(1.0)


def test_identify_unknown_person():
    target = np.array([1.0, 0.0])

    profiles = {
        "alice": np.array([0.0, 1.0]),
        "bob": np.array([-1.0, 0.0]),
    }

    name, score = speakerid.identify(
        target,
        profiles,
        threshold=0.75,
    )

    assert name is None
    assert score < 0.75


def test_identify_empty_profiles():
    target = np.array([1.0, 0.0])

    name, score = speakerid.identify(
        target,
        {},
    )

    assert name is None
    assert score == 0.0


def test_identify_custom_threshold():
    target = np.array([1.0, 0.0])

    profiles = {
        "yolezz": np.array([1.0, 1.0]),
    }

    name, score = speakerid.identify(
        target,
        profiles,
        threshold=0.5,
    )

    assert name == "yolezz"


def test_identify_invalid_threshold():
    target = np.array([1.0, 0.0])

    with pytest.raises(ValueError):
        speakerid.identify(
            target,
            {},
            threshold=-0.1,
        )

    with pytest.raises(ValueError):
        speakerid.identify(
            target,
            {},
            threshold=1.1,
        )
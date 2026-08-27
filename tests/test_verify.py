import numpy as np
import pytest

import speakerid


def test_verify_identical_embeddings():
    embedding = np.array([1.0, 2.0, 3.0])

    assert speakerid.verify(
        embedding,
        embedding,
    )


def test_verify_different_embeddings():
    first = np.array([1.0, 0.0])
    second = np.array([0.0, 1.0])

    assert not speakerid.verify(
        first,
        second,
    )


def test_verify_custom_threshold():
    first = np.array([1.0, 0.0])
    second = np.array([1.0, 1.0])

    assert speakerid.verify(
        first,
        second,
        threshold=0.7,
    )

    assert not speakerid.verify(
        first,
        second,
        threshold=0.8,
    )


def test_verify_invalid_threshold():
    first = np.array([1.0, 0.0])
    second = np.array([1.0, 0.0])

    with pytest.raises(ValueError):
        speakerid.verify(
            first,
            second,
            threshold=-0.1,
        )

    with pytest.raises(ValueError):
        speakerid.verify(
            first,
            second,
            threshold=1.1,
        )
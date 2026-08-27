import numpy as np
import pytest

import speakerid


def test_compare_identical_embeddings():
    embedding = np.array([1.0, 2.0, 3.0])

    score = speakerid.compare(
        embedding,
        embedding,
    )

    assert score == pytest.approx(1.0)


def test_compare_different_embeddings():
    first = np.array([1.0, 0.0])
    second = np.array([0.0, 1.0])

    score = speakerid.compare(first, second)

    assert score == pytest.approx(0.0)


def test_compare_opposite_embeddings():
    first = np.array([1.0, 0.0])
    second = np.array([-1.0, 0.0])

    score = speakerid.compare(first, second)

    assert score == pytest.approx(-1.0)


def test_compare_different_shapes():
    first = np.array([1.0, 2.0])
    second = np.array([1.0, 2.0, 3.0])

    with pytest.raises(ValueError):
        speakerid.compare(first, second)


def test_compare_zero_embedding():
    first = np.array([0.0, 0.0])
    second = np.array([1.0, 0.0])

    with pytest.raises(ValueError):
        speakerid.compare(first, second)
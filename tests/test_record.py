import inspect

import speakerid


def test_record_exists():
    assert callable(speakerid.record)


def test_record_signature():
    signature = inspect.signature(speakerid.record)

    assert "output" in signature.parameters
    assert "duration" in signature.parameters
    assert "sample_rate" in signature.parameters
    assert "channels" in signature.parameters
    assert "device" in signature.parameters
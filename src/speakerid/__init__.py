"""
SpeakerID - Python library for speaker recognition.
"""

from ._version import (
    __author__,
    __author_email__,
    __build__,
    __copyright__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __banana__,
)

from .recording import record
from .phrases import get_phrases, set_phrases
from .audio import clean

__all__ = [
    "__title__",
    "__description__",
    "__url__",
    "__version__",
    "__build__",
    "__author__",
    "__author_email__",
    "__license__",
    "__copyright__",
    "__banana__",
    "record",
    "set_phrases",
    "get_phrases",
    "clean",
]


def version() -> str:
    """
    Return the current SpeakerID version.

    Returns:
        str: Current package version.
    """
    return __version__


def help() -> None:
    """
    Display basic information about SpeakerID.
    """
    print(
        f"""SpeakerID {__version__}

Python library for speaker recognition.

Available functions:
    record()
    set_phrases()
    get_phrases()
    enroll()

    clean()
    augment()

    encode()
    compare()
    identify()
    verify()

    get_profile()
    list_profiles()
    add_sample()
    remove_sample()
    build_profile()
    delete_profile()

    save()
    load()
"""
    )
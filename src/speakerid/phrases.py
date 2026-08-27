_phrases: dict[str, list[str]] = {}

_DEFAULT_LANGUAGE = "en"


def set_phrases(
    phrases: list[str],
    language: str = _DEFAULT_LANGUAGE,
) -> None:
    _phrases[language] = list(phrases)


def get_phrases(
    language: str = _DEFAULT_LANGUAGE,
) -> list[str]:
    return list(_phrases.get(language, []))
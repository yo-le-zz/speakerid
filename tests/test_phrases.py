import speakerid


def test_set_and_get_phrases():
    phrases = [
        "Bonjour.",
        "Comment allez-vous ?",
    ]

    speakerid.set_phrases(phrases, "fr")

    assert speakerid.get_phrases("fr") == phrases


def test_default_language():
    phrases = [
        "Hello.",
        "How are you?",
    ]

    speakerid.set_phrases(phrases)

    assert speakerid.get_phrases() == phrases
    assert speakerid.get_phrases("en") == phrases


def test_unknown_language():
    assert speakerid.get_phrases("unknown") == []


def test_set_phrases_copies_input():
    phrases = ["Bonjour."]

    speakerid.set_phrases(phrases, "fr")

    phrases.append("Salut.")

    assert speakerid.get_phrases("fr") == ["Bonjour."]


def test_get_phrases_returns_copy():
    speakerid.set_phrases(["Bonjour."], "fr")

    phrases = speakerid.get_phrases("fr")
    phrases.append("Salut.")

    assert speakerid.get_phrases("fr") == ["Bonjour."]
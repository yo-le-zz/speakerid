import speakerid


def test_title():
    assert speakerid.__title__ == "speakerid"


def test_description():
    assert speakerid.__description__ == "Python library for speaker recognition."


def test_url():
    assert speakerid.__url__ == "https://github.com/yo-le-zz/speakerid"


def test_author():
    assert speakerid.__author__ == "yo-le-zz"


def test_author_email():
    assert speakerid.__author_email__ == "yolezz.secret@gmail.com"


def test_license():
    assert speakerid.__license__ == "MIT"


def test_copyright():
    assert speakerid.__copyright__ == "Copyright yo-le-zz"


def test_banana():
    assert speakerid.__banana__ == "🍌"
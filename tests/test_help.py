import speakerid


def test_help(capsys):
    speakerid.help()

    output = capsys.readouterr().out

    assert "SpeakerID" in output
    assert speakerid.__version__ in output
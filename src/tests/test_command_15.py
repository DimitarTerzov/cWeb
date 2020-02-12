import pytest

from problem_15.validator_15 import command15


INCORRECT_USE ="word~word\nword ~ word\nword~~ word"
CORRECT_USE = "word~ word\nword ~word"


def create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    f = d / "tilde.trs"
    return f


def test_command15_incorrect_use(tmp_path):
    file_ = create_file(tmp_path)
    file_.write_text(INCORRECT_USE)
    found = command15(file_)
    print(found)
    assert len(found) == 3


def test_command15_correct_use(tmp_path):
    file_ = create_file(tmp_path)
    file_.write_text(CORRECT_USE)
    found = command15(file_)
    print(found)
    assert len(found) == 0


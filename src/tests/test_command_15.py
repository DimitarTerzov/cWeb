import pytest

from problem_15.validator_15 import command15


CONTENT =[
    "word~word\n",
    "word ~ word\n",
    "word~~ word\n",
    "word~ word\n",
    "word ~word\n",
    " ~word\n",
    "hello word~ word\n",
    "hello word~ ."
]


@pytest.fixture
def file_with_tildes(tmpdir):
    file_ = tmpdir.mkdir("sub").join("tilde.trs")
    with open(file_, 'a') as f:
        for line in CONTENT:
            f.write(line)
    return file_


def test_command15(file_with_tildes):
    found = command15(file_with_tildes)
    with open(file_with_tildes) as file_:
        for line in file_.readlines():
            print(line.rstrip())
    for value in found.values():
        assert "word~ word" not in value
        assert "word ~word" not in value
        assert "hello word~ ." not in value
        assert "hello word~ word" not in value
        assert " ~word" not in value

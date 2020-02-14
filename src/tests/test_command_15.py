import pytest

from problem_15.validator_15 import command15


CONTENT =[
    "word~word\n",
    "word ~ word\n",
    "word~~ word\n",
    "word~ word\n",
    "hello world~word\n",
    "word ~word\n",
    " ~word\n",
    "hello word~ word\n",
    "hello word~ .\n",
    "hello world~.\n",
    "hello hello~. Where\n",
    " ~ word\n",
    "word ~ \n",
    "hello ~~.\n",
    "~~hi"
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
    print(found)

    assert "word~word" in found[0]
    assert "world~word" in found[4]
    assert "world~." in found[9]
    assert "hello~." in found[10]
    assert "word ~ word" in found[1]
    assert " ~ word" in found[11]
    assert "word ~ " in found[12]
    assert "word~~ word" in found[2]
    assert "hello ~~" in found[13]
    assert "~~hi" in found[14]
    assert len(found) == 10
    assert 0

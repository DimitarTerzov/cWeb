import pytest

from problem_15.validator_15 import command15


CONTENT =[
    "word~word\n",      # 0
    "word ~ word\n",    # 1
    "word~~ word\n",    # 2
    "word~ word\n",     # 3
    "hello world~word\n",      # 4
    "word ~word\n",            # 5
    " ~word\n",                # 6
    "hello word~ word\n",      # 7
    "hello word~ .\n",         # 8
    "hello world~.\n",         # 9
    "hello hello~. Where\n",   # 10
    " ~ word\n",               # 11
    "word ~ \n",               # 12
    "hello ~~.\n",             # 13
    "~~hi\n",                  # 14
    "where ~Tilde milde\n",           # 15
    "So,~ not allowed\n",            # 16
    "also .~ not allowed\n",          # 17
    "this ,~. too not allowed\n",     # 18
    "filler #uh~ tilde not allowed\n"   # 19
    "filler #uhaa~. dot\n"              # 20
    "filler #uha~a bla\n"               # 21
    "[noise]~. ala bala\n"               # 22
    "ala ~. bala"                       # 23
]


@pytest.fixture
def file_with_tildes(tmpdir):
    file_ = str(tmpdir.mkdir("sub").join("tilde.trs"))
    with open(file_, 'a') as f:
        for line in CONTENT:
            f.write(line)
    return file_


def test_command15(file_with_tildes):
    found = command15(file_with_tildes)
    keys = sorted(found.keys())
    for key in keys:
        print(key, found[key])

    assert "word~word" in found[0]
    assert "word ~ word" in found[1]
    assert "word~~ word" in found[2]
    assert "world~word" in found[4]
    assert not 9 in found
    assert not 10 in found
    assert " ~ word" in found[11]
    assert "word ~ " in found[12]
    assert "hello ~~" in found[13]
    assert "~~hi" in found[14]
    assert not 15 in found
    assert ",~" in found[16]
    assert ".~" in found[17]
    assert ",~." in found[18]
    assert "#uh~" in found[19]
    assert "#uhaa~" in found[20]
    assert "#uha~" in found[21]
    assert "]~." in found[22]
    assert "~." in found[23]
    assert len(found) == 16

    assert 0

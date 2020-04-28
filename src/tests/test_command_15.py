# -*- coding: utf-8 -*-
from __future__ import print_function

from command_15.validator_15 import command15
from utils import temporary_file


CONTENT =[
    u'<Section type="report" startTime="0" endTime="2642.252">\n',         # 0
    u'[music]&lt;lang:TSM&gt;別跑，你別跑&lt;/lang:TSM&gt;~不曾讓任何\n',    # 1
    u'我~，單無雙，全力奔馳近三十三年\n',    # 2
    u'我。~單無雙，全力奔馳近三十三年\n',    # 3
    u'我，單~無雙，全力奔馳近三十三年\n',    # 4
    u'~我，單無雙，全力奔馳近三十三年\n',    # 5
    u'我，單無雙，全力奔 ~ 馳近三十三年\n',   # 6
    u'我，單無雙，全力奔馳~ 近三十三年\n',    # 7
    u'我，單無雙，全 ~力奔馳近三十三年\n',    # 8
    u'其實不瞞大家說我買好了~~\n',    # 9
    u'其實不瞞大家說~~我買好了\n',    # 10
    u'其實不瞞大家說我買好了~？\n',    # 11
    u'其實不瞞大家說我買好~ ！\n',      # 12
    u'~~我買好了\n',                           # 13
]
EXCLUDE = [
    0, 1, 2, 3, 4, 5, 11
]
CATCH = [
    6, 7, 8, 9, 10, 12, 13
]


def test_command15(tmpdir):
    file_ = temporary_file(tmpdir, CONTENT)
    found = command15(file_)

    for key in sorted(found.keys()):
        print(key, found[key])

    for row in EXCLUDE:
        assert row not in found

    for row in CATCH:
        assert row in found

    #assert 0

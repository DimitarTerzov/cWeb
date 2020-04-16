# -*- coding: utf-8 -*-
from __future__ import print_function

import pytest

from utils import temporary_file
from command_7.validator_7 import command7


CONTENT = [
    u'<Speaker id="spk75" name="speaker#56"/>\n',    # 1
    u'<Speaker id="spk76" name="speaker#57"/>\n',    # 2
    u'<Section type="report" startTime="0" endTime="2631.216">\n'    # 3
    u"#啊，希望大家都能夠健康平安的一個應應做法。\n",    # 4
    u"其實除了有，#啊，三十個國家地區之外呢，\n",          # 5
    u"#啊所有的菩薩們呢，人人的這個自心\n",                    # 6
    u"也特別調配了一個#啊，養生祈福飲。\n",                    # 7
    u"也特別調配了一個 #呃\n",                                         # 8
    u"也特別調配了一個#飲，養生祈福飲。\n",                    # 9
    u"也特別調配了一個#祈，養生祈福飲。\n",                    # 10
    u"也特別調配了一個#呃《》養生祈福飲。\n",                 # 11
    u"也特別調配了一：#嗯，養生祈福飲。\n",                    # 12
    u'[overlap]那麼冷，[overlap]#啊。\n',                        # 13
    u'#啊 所有的菩薩們呢\n',                                             # 14
    u"也特別調配了一個#呃\n",                                          # 15
    u'個#呃#呃尖的東西把它刮\n',                                      # 16
    u'</Section>'                                                             # 17
]
EXCLUDE = [1, 2, 3, 4, 5, 6, 7, 13, 15, 16, 17]
CATCH = [8, 9, 10, 11, 12, 14]


def test_command_7(tmpdir):
    file_ = temporary_file(tmpdir, CONTENT)
    found = command7(file_)

    keys = sorted(found.keys())
    for key in keys:
        print(key, found[key])

    for item in EXCLUDE:
        assert item not in found

    for item in CATCH:
        assert item in found

    #assert 0

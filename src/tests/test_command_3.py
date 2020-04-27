# -*- coding: utf-8 -*-
from __future__ import print_function

from utils import temporary_file
from command_3.validator_3 import command3


CONTENT = [
    u'[laughter]好，現在我們來示範金蟬脫殼\n',                                               # 0
    u'<Section type="report" startTime="0" endTime="2642.252">\n',    # 1
    u'[music]&lt;lang:TSM&gt;別跑，你別跑&lt;/lang:TSM&gt;\n',                  # 2
    u'下界(())熱門候選人((柯有正))。[noise]\n',                                                # 3
    u'[laugh]好，現在我們來示範金蟬脫殼\n',                                                   # 4
    u'[laugh][laugh]好，現在我們來示範金蟬脫殼\n',                                        # 5
    u'[laughter]好，現在我們來示範金蟬脫殼\n',                                               # 6
    u'[laugh]現在[laugh]好，現在我們來示範金蟬脫殼\n',                                   # 7
]
EXCLUDE = [
    0, 1, 2, 3, 4, 7
]
CATCH = [
    5, 6
]


def test_command_3(tmpdir):
    file_ = temporary_file(tmpdir, CONTENT)
    found = command3(file_)

    for key in sorted(found.keys()):
        print(key, found[key])

    for row in EXCLUDE:
        assert row not in found

    for row in CATCH:
        assert row in found

    #assert 0

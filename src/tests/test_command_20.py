# -*- coding: utf-8 -*-
from __future__ import print_function

import pytest

from utils import temporary_file
from command_20.validator_20 import command20


CONTENT = [
    u'<Speakers>\n',                                                         # 0
    u'<Speaker id="spk14" name="Paul Ruseau"/>\n',    # 1
    u'</Speakers>\n',                                                        # 2
    u'<Episode>\n',                                                           # 3
    u'<Section type="report" startTime="0" endTime="3489.288">\n',        # 4
    u'<Turn speaker="spk2" startTime="86.623" endTime="88.487">\n',    # 5
    u'<Sync time="86.623"/>\n',                                                                     # 6
    u"&lt;initial&gt; error1 &lt;/initial&gt;&gt; Good evening once again.\n",   # 7
    u'<Sync time="88.487"/>\n',                                                                      # 8
    u"<initial> error2 </initial>  And we're here to once again\n",                  # 9
    u'</Turn>\n',                                                                                               # 10
    u'<Turn speaker="spk3" startTime="85.725" endTime="86.623">\n',      # 11
    u'<Sync time="85.725"/>\n',                                                                      # 12
    u'[lipsmack] <lang:Spanish> ČSSD wrong tags in code error 9 </lang:Spanish> Over\n',  # 13
    u'<Sync time="86.623"/>\n',                                                                                               # 14
    u'Flag of the United <lang:respect> States of America\n',                                                   # 15
    u'<Sync time="88.487"/>\n',                                                                              # 16
    u"We strongly believe it l\'&lt;initial&gt; ONU &lt;/initial&gt; is important,\n",    # 17
    u'<Sync time="94.373"/>\n',                                                                              # 18
    u'<Sync time="3415.916"/>\n',                                                               # 19
    u'Your presence here to <lang:body> listen to the ten candidates.\n',    # 20
    u'</Turn>\n',                                                                           # 21
    u'<Turn startTime="3415.916" endTime="3416.904">\n',    # 22
    u'<Sync time="3415.916"/>\n',    # 23
    u'</Turn>\n',         # 24
    u'</Section>\n',    # 25
    u'</Episode>\n',   # 26
    u'</Trans>\n',       # 27
]
EXCLUDE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14,
                    16, 17, 18,  19, 21, 22, 23, 24, 25, 26, 27]
CATCH = [9, 13, 15, 20]


def test_command_20(tmpdir):
    file_ = temporary_file(tmpdir, CONTENT)
    found = command20(file_)

    for key in sorted(found.keys()):
        print(key, found[key])

    for row in EXCLUDE:
        assert row not in found

    for row in CATCH:
        assert row in found

    #assert 0

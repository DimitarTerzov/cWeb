# -*- coding: utf-8 -*-
from __future__ import print_function

import pytest

from utils import temporary_file
from command_4.validator_4 import command4


CONTENT = [
    u'透過&lt;initial&gt;FB&lt;/initial&gt;還有\n',       # 0
    u'&lt;initial&gt; N &lt;/initial&gt;是諾貝爾，\n',    # 1
    u'是&lt;initial&gt; L &lt;/initial&gt;\n',                 # 2
    u'最重要是我們第一個就是用&lt;initial&gt;IT&lt;/initial&gt;的科技哦\n',    # 3
    u'個就是用 &lt;initial&gt;IT&lt;/initial&gt; 的科技哦\n',                           # 4
    u'所以我們在門口有一個&lt;initial&gt;QRC&lt;/initial&gt;，\n',                # 5
    u'是 &lt;initial&gt;L&lt;/initial&gt;\n',                # 6
    u'透過&lt;initial&gt;FB&lt;/initial&gt; 還有\n',    # 7
    u'&lt;initial&gt; N &lt;/initial&gt; 是諾貝爾\n',    # 8
    u'用&lt;initial&gt;IT&lt;/initial&gt;\n',                # 9
    u'&lt;initial&gt;W. E. B.&lt;/initial&gt;是諾貝\n',    # 10
    u'是諾貝&lt;initial&gt;W! E. B.&lt;/initial&gt;\n',    # 11
    u'是諾貝&lt;initial&gt;W E B&lt;/initial&gt;，\n',    # 12
    u'是諾&lt;initial&gt;W?EB&lt;/initial&gt;是諾\n',    # 13
    u'是諾&lt;initial&gt;W!&lt;/initial&gt;\n',               # 14
    u'&lt;initial&gt;Ph.D.&lt;/initial&gt;是諾\n',           # 15
    u'猴頭菇&lt;initial&gt;SO&lt;/initial&gt;&lt;lang:English&gt;Okay&lt;/lang:English&gt;醬就好了。\n',    # 16
]
EXCLUDE =[0, 3, 5, 9, 10, 15, 16]
CATCH = [1, 2, 4, 6, 7, 8, 11, 12, 13, 14]

def test_command4(tmpdir):
    file_ = temporary_file(tmpdir, CONTENT)
    found = command4(file_)

    keys = sorted(found.keys())
    print(len(keys))
    for key in keys:
        print(key, found[key])

    for item in EXCLUDE:
        assert item not in found

    for item in CATCH:
        assert item in found

    #assert 0

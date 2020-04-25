# -*- coding: utf-8 -*-
from __future__ import print_function

from utils import temporary_file
from command_5.validator_5 import command5


CONTENT = [
    u'<Turn startTime="3082.959" endTime="3084.519">\n', # 0
    u'<Sync time="3082.959"/>\n', # 1
    u'[overlap]&lt;lang:English&gt;Okay&lt;/lang:English&gt;醬就好了。\n', # 2
    u'</Turn>\n', # 3
    u'<Turn startTime="3086.814" endTime="3087.707">\n', # 4
    u'<Sync time="3086.814"/>\n', # 5
    u'還有&lt;lang:English&gt;YouTube&lt;/lang:English&gt;的直播平臺，\n', # 6
    u'<Sync time="3093.168"/>\n', # 7
    u'還有&lt;lang:English&gt;YouTube &lt;/lang:English&gt;！的直播平臺\n', # 8
    u'<Sync time="3131.57"/>\n', # 9
    u'還有 &lt;lang:English&gt;YouTube&lt;/lang:English&gt;，的直播平臺\n', # 10
    u'<Sync time="3148.785"/>\n', # 11
    u'還有&lt;lang:English&gt; YouTube&lt;/lang:English&gt;的直播平臺，\n', #  12
    u'<Sync time="3150.738"/>\n', # 13
    u'因為呢，&lt;lang:English&gt;(())&lt;/lang:English&gt;\n', # 14
    u'<Sync time="3170.236"/>\n', # 15
    u'&lt;lang:English&gt;Okay&lt;/lang:English&gt;醬就好了。[laugh]\n', # 16
    u'<Sync time="3171.857"/>\n', # 17
    u'醬就&lt;lang: Foreign&gt; ČSSD tag spacing 6 &lt;/lang:Foreign&gt;醬就好了。\n', # 18
    u'<Sync time="3184.345"/>\n', # 19
    u'因為呢，&lt;lang:English&gt;(()) &lt;/lang:English&gt;\n', # 20
    u'<Sync time="3197.754"/>\n', # 21
    u'因為呢，&lt;lang:English&gt; (())&lt;/lang:English&gt;\n', # 22
    u'<Sync time="3207.962"/>\n', # 23
    u"因為呢，&lt;lang:English&gt;(())&lt;/lang:english&gt;\n", # 24
    u'<Sync time="3213.568"/>\n', # 25
    u'<lang:Spanish>ČSSD wrong tags in code error 9</lang:Spanish>\n', # 26
    u'<Sync time="3224.352"/>\n', # 27
    u'&lt;lang:Foreign&gt;&gt;double > error 10 ČSSD&lt;/lang:Foreign&gt;\n', # 28
    u'<Sync time="3234.082"/>\n', # 29
    u'&lt;lang:Foreign&gt;error 11 ČSSD？&lt;/lang:Foreign&gt;\n', # 30
    u'</Turn>\n', # 31
    u'<Turn startTime="3362.063" endTime="3364.044">\n', # 32
    u'<Sync time="3246.403"/>\n', # 33
    u'&lt;lang:English&gt;&lt;/lang:English&gt;\n', # 34
    u'<Sync time="3270.24"/>\n', # 35
    u'或是阿米&lt;lang:English&gt;at life&lt;/Lang:English&gt;或\n', # 36
    u'<Sync time="3336.788"/>\n', # 37
    u'&lt;lang:English&gt;word, word (()) <initial> ČSSD <initial>, etc&lt;/lang:English&gt;\n', # 38
    u'<Sync time="3349.75"/>\n', # 39
    u"&lt;lang:English&gt;ČSSD perspective&lt;lang:English&gt;lang tag inside lang \
    tag&lt;/lang:English&gt;ČSSD and voice&lt;/lang:English&gt;\n", # 40
    u'<Sync time="3082.959"/>\n', # 41
    u'醬就好了&lt;lang:English&gt;Okay&lt;/lang:English&gt;[applause]。\n', # 42
    u'</Turn>\n', # 43
    u'醬就好了&lt;lang:English&gt;&gt;Okay&lt;/lang:English&gt;。\n',   # 44
    u'&lt;lang:Japanese&gt;おひさ[overlap]&lt;/lang:Japanese&gt;。\n', # 45
]

EXCLUDE = [
    0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 14,
    15, 16, 17, 19, 21, 23, 25, 26, 27,
    29, 31, 32, 33, 35, 37, 38, 39, 41, 42, 43, 45
]

CATCH = [
    8, 10, 12, 18, 20, 22, 24,
    28, 30, 34, 36, 40, 44
]


def test_command5(tmpdir):
    file_ = temporary_file(tmpdir, CONTENT)
    found = command5(file_)

    for key in sorted(found.keys()):
        print(key, found[key])


    for row in EXCLUDE:
        assert row not in found

    for row in CATCH:
        assert row in found

    #assert 0

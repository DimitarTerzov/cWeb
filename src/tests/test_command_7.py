# -*- coding: utf-8 -*-
from __future__ import print_function

import pytest

from utils import temporary_file
from command_7.validator_7 import command7


CONTENT = [
    u'<Speaker id="spk75" name="speaker#56" check="no" type="female" dialect="native" accent="" scope="local"/>\n', # 1
    u'<Speaker id="spk76" name="speaker#57" check="no" type="female" dialect="native" accent="" scope="local"/>\n', # 2
    u'<Section type="report" startTime="0" endTime="2631.216">\n' # 3
    u"I was on # uh Paul Finebaum's show\n",    # 4
    u"I love that hire. #um We kind of~~we've kind\n",    # 5
    u"Joe Morehead maybe out of Mississippi State after this, #uhh,\n",    # 6
    u"or out east and, #Eh, Lane would be\n",    # 7
    u"happen and, #UH,\n",                       # 8
    u"#aH but yeah, I don't know\n",             # 9
    u"here, #hm, Shane, Ole Miss\n",             # 10
    u"#um I think you got to give ~,\n",         # 11
    u"#uH Why do you want to stand\n",           # 12
    u"really well, so #uh.\n",                   # 13
    u"previously .#uh at Missouri\n",            # 14
    u"on a.#uh previous podcast\n",              # 15
    u"speaking of tangled ,#er webs, Shane,\n",  # 16
    u"I ain't,#uh go do any more\n",             # 17
    u"He's word#ah doing these commercials\n",   # 18
    u"well, #uhword we got a first-round\n",     # 19
    u"Set #øh Men In Black,\n",                  # 20
    u"and, #um, I don't know with Bama\n",       # 21
    u"daje się #mmm we znaki rotawirus\n",       # 22
    u"[breath] #yyy taka łuna [breath].\n",      # 23
    u"then #uh- who knows, maybe \n",            # 24
    u"So #uh and I don't think\n",               # 25
    u"#~ Thank thank God,\n",                    # 26
    u"because, #yes~ , he injured his neck,\n",  # 27
    u"I think, #uh~, I don't necessarily\n",     # 28
    u"#uh— but this is just a wacky\n",          # 29
    u"team, uh does that weigh on your\n",       # 30
    u"I'm not um making too much out of that\n", # 31
    u"Lawrence is gonumna be there\n",           # 32
    u"acted liuhke the question wasn't asked.\n",# 33
    u'ใช่ค่ะ่ยงแล้วเพราะว่าขึ้นชื่ออยู่แล้วแล้วก็ #อือ ตามความเข้าใจของตันตันนะคะ\n', #34
    u'งนะคะก็เลยได้รวบรวมผู้เชี่ยวชาญแล้วก็ #อ่า ผู้แทนของชาวบ้าน\n', # 35
    u'ซึ่งตอนนี้นะคะที่นี่ก็ยังมีสถานที่แนะนำ #เอ่อ วัฒนธรรมและ\n', # 36
    u'</Section>'                                # 37
]


def test_command_7(tmpdir):
    file_ = temporary_file(tmpdir, CONTENT)
    found = command7(file_)

    keys = sorted(found.keys())
    for key in keys:
        print(key, found[key])

    assert 1 not in found
    assert 2 not in found
    assert 3 not in found
    assert 4 in found
    assert 5 not in found
    assert 6 in found
    assert 7 in found
    assert 8 in found
    assert 9 in found
    assert 10 not in found
    assert 11 not in found
    assert 12 in found
    assert 13 not in found
    assert 14 in found
    assert 15 in found
    assert 16 in found
    assert 17 in found
    assert 18 in found
    assert 19 in found
    assert 20 in found
    assert 21 not in found
    assert 22 in found
    assert 23 in found
    assert 24 not in found
    assert 25 not in found
    assert 26 not in found
    assert 27 not in found
    assert 28 not in found
    assert 29 not in found
    assert 30 in found
    assert 31 in found
    assert 32 not in found
    assert 33 not in found
    assert 34 in found
    assert 35 in found
    assert 36 in found

    #assert 0

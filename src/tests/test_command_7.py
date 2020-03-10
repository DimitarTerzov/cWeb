# -*- coding: utf-8 -*-
from __future__ import print_function

import pytest

from utils import temporary_file
from command_7.validator_7 import command7


CONTENT = [
    u'<Speaker id="spk75" name="speaker#56" check="no" type="female" dialect="native" accent="" scope="local"/>\n', # 0
    u'<Speaker id="spk76" name="speaker#57" check="no" type="female" dialect="native" accent="" scope="local"/>\n', # 1
    u'<Section type="report" startTime="0" endTime="2631.216">\n' # 2
    u"I was on # uh Paul Finebaum's show\n",    # 3
    u"I love that hire. #um We kind of~~we've kind\n",    # 4
    u"Joe Morehead maybe out of Mississippi State after this, #uhh,\n",    # 5
    u"or out east and, #Eh, Lane would be\n",    # 6
    u"happen and, #UH,\n",                       # 7
    u"#aH but yeah, I don't know\n",             # 8
    u"here, #hm, Shane, Ole Miss\n",             # 9
    u"#um I think you got to give ~,\n",         # 10
    u"#uH Why do you want to stand\n",           # 11
    u"really well, so #uh.\n",                   # 12
    u"previously .#uh at Missouri\n",            # 13
    u"on a.#uh previous podcast\n",              # 14
    u"speaking of tangled ,#eh webs, Shane,\n",  # 15
    u"I ain't,#uh go do any more\n",             # 16
    u"He's word#ah doing these commercials\n",   # 17
    u"well, #uhword we got a first-round\n",     # 18
    u"Set #øh Men In Black,\n",                  # 19
    u"and, #um, I don't know with Bama\n",       # 20
    u"daje się #mmm we znaki rotawirus\n",       # 21
    u"[breath] #yyy taka łuna [breath].\n",      # 22
    u"then #uh- who knows, maybe \n",            # 23
    u"So #uh and I don't think\n",               # 24
    u"#~ Thank thank God,\n",                    # 25
    u"because, #yes~ , he injured his neck,\n",  # 26
    u"I think, #uh~, I don't necessarily\n",     # 27
    u"#uh— but this is just a wacky\n",          # 28
    u"team, uh does that weigh on your\n",       # 29
    u"I'm not um making too much out of that\n", # 30
    u"Lawrence is gonumna be there\n",           # 31
    u"acted liuhke the question wasn't asked.\n",# 32
    u'</Section>'                                # 33
]


def test_command_7(tmpdir):
    file_ = temporary_file(tmpdir, CONTENT)
    found = command7(file_)

    keys = sorted(found.keys())
    for key in keys:
        print(key, found[key])

    assert not 0 in found
    assert not 1 in found
    assert 3 in found
    assert not 4 in found
    assert 5 in found
    assert 6 in found
    assert 7 in found
    assert 8 in found
    assert not 9 in found
    assert not 10 in found
    assert 11 in found
    assert not 12 in found
    assert 13 in found
    assert 14 in found
    assert 15 in found
    assert 16 in found
    assert 17 in found
    assert 18 in found
    assert 19 in found
    assert not 20 in found
    assert 21 in found
    assert 22 in found
    assert not 23 in found
    assert not 24 in found
    assert not 25 in found
    assert not 26 in found
    assert not 27 in found
    assert not 28 in found
    assert 29 in found
    assert 30 in found
    assert not 31 in found
    assert not 32 in found

    assert 0

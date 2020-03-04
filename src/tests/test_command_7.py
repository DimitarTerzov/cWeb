# -*- coding: utf-8 -*-
from __future__ import print_function

import pytest

from utils import temporary_file
from command_7.validator_7 import command7


CONTENT = [
    u"I was on # uh Paul Finebaum's show\n",    # 0
    u"I love that hire. #um We kind of~~we've kind\n",    # 1
    u"Joe Morehead maybe out of Mississippi State after this, #uhh,\n",    # 2
    u"or out east and, #Eh, Lane would be\n",    # 3
    u"happen and, #UH,\n",                       # 4
    u"#aH but yeah, I don't know\n",             # 5
    u"here, #hm, Shane, Ole Miss\n",             # 6
    u"#um I think you got to give ~,\n",         # 7
    u"#uH Why do you want to stand\n",           # 8
    u"really well, so #uh.\n",                   # 9
    u"previously .#uh at Missouri\n",            # 10
    u"on a.#uh previous podcast\n",              # 11
    u"speaking of tangled ,#eh webs, Shane,\n",  # 12
    u"I ain't,#uh go do any more\n",             # 13
    u"He's word#ah doing these commercials\n",   # 14
    u"well, #uhword we got a first-round\n",     # 15
    u"Set #øh Men In Black,\n",                  # 16
    u"and, #um, I don't know with Bama\n",       # 17
    u"daje się #mmm we znaki rotawirus\n",       # 18
    u"[breath] #yyy taka łuna [breath].\n",      # 19
    u"then #uh, who knows, maybe \n",            # 20
    u"So #uh and I don't think\n",               # 21
    u"#~ Thank thank God,\n",                    # 22
    u"because, #yes~ , he injured his neck,\n",    # 23
    u"I think, #uh~, I don't necessarily\n",     # 24
    u"#uh, but this is just a wacky\n",          # 25
    u"team, uh does that weigh on your\n",       # 26
    u"I'm not um making too much out of that\n", # 27
    u"Lawrence is gonumna be there\n",           # 28
    u"acted liuhke the question wasn't asked."   # 29
]


def test_command_7(tmpdir):
    file_ = temporary_file(tmpdir, CONTENT)
    found = command7(file_)

    keys = sorted(found.keys())
    for key in keys:
        print(key, found[key])

    assert 0 in found
    assert not 1 in found
    assert 2 in found
    assert 3 in found
    assert 4 in found
    assert 5 in found
    assert not 6 in found
    assert not 7 in found
    assert 8 in found
    assert not 9 in found
    assert 10 in found
    assert 11 in found
    assert 12 in found
    assert 13 in found
    assert 14 in found
    assert 15 in found
    assert 16 in found
    assert not 17 in found
    assert 18 in found
    assert 19 in found
    assert not 20 in found
    assert not 21 in found
    assert not 22 in found
    assert not 23 in found
    assert not 24 in found
    assert not 25 in found
    assert 26 in found
    assert 27 in found
    assert not 28 in found
    assert not 29 in found

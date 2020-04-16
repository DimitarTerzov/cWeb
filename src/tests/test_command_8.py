# -*- coding: utf-8 -*-
from __future__ import print_function

from utils import temporary_file
from command_8.validator_8 import command8


CONTENT = [
    u'((根))你好。#啊，今天呢，\n',    # 0
    u'裡面呢((央))跟肉呢，\n',             # 1
    u'看到過，((下菜場里))#呃，\n',    # 2
    u'中藥使用的(())是非常多的。\n',    # 3
    u'在新#額(())。\n',                        # 4
    u'(())[overlap][laugh]所以我說因緣不可思議，\n',    # 5
    u'善變化。(())就素\n',                                             # 6
    u'三(())[laugh],\n',                                                 # 7
    u'這是如素者出門在外常遇到的挑戰，(())。\n',           # 8
    u'[laugh](())這種緣。\n',                                         # 9
    u'&lt;lang:Foreign&gt; (()) &lt;/lang:Foreign&gt;\n',    # 10
    u'就是就是 [overlap] (()) 的印刷術、\n',                          # 11
    u'大部分 (()) 而已。\n',                                                   # 12
    u'&lt;lang:English&gt; ((nature teachers)) &lt;/lang:English&gt;\n',    # 13
    u'是&lt;lang:English&gt;(())&lt;/lang:English&gt;然後\n',                      # 14
    u'那徹底 (()) 了。\n',                # 15
    u'廣播可以呢進入了 (())，\n',    # 16
    u'(()) 好幾道門檻要過，\n',       # 17
    u'了那個(( 刀兵劫 ))了，\n',      # 18
    u'了那個(( 刀兵劫))了，\n',       # 19
    u'了那個((刀兵劫 ))了，\n',       # 20
    u'是<lang:English>(())</lang:English>然後\n',    # 21
    u'三(())[ laugh]！\n',    # 22
    u'三(())[laugh ]。\n',    # 23
    u'三(())[ laugh ]．\n',    # 24
    u'三(())[laugh]．\n',    # 25
    u'淡化[non-speech][overlap]\n',      # 26
    u'淡化((non-speech))[overlap]\n',    # 27
    u'我自己也有((休，休旅車))，\n',        # 28
    u'[music]　'                                     # 29
]
EXCLUDE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 21, 25, 26, 27, 28, 29]
CATCH = [11, 12, 15, 16, 17, 18, 19, 20, 22, 23, 24]


def test_command_8(tmpdir):
    file_ = temporary_file(tmpdir, CONTENT)
    found = command8(file_)

    for key in sorted(found.keys()):
        print(key, found[key])

    for item in EXCLUDE:
        assert item not in found

    for item in CATCH:
        assert item in found

    #assert 0

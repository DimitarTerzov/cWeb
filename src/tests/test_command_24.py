# -*- coding: utf-8 -*-
from __future__ import print_function

from utils import temporary_file
from command_24.validator_24 import command24


CONTENT = [
    u'<Turn startTime="0" endTime ="14.781" speaker="spk1">\n',    # 1
    u'<Sync time="0"/>\n',                                         # 2
    u'[overlap]\n'                                                 # 3
    u'</Turn>\n',                                                  # 4
    u'<Turn speaker="spk2" startTime="14.781" endTime=" 21.081">\n',  # 5
    u'<Sync time=" 15.781"/>\n',                                      # 6
    u'[noise] [music] 물러나시오! 임금님 행차하신다.\n',                # 7
    u'</Turn>\n',                                                     # 8
    u'<Turn speaker="spk3" startTime="21.081 " endTime="32.282">\n',  # 9
    u'<Sync time= "28.081"/>\n',                                      # 10
    u'[laugh] [applause] 보이느냐? 나의 이 멋진 옷이! [laugh]\n',       # 11
    u'</Turn>\n',                                                     # 12
    u'<Turn speaker="spk4" startTime="32.282" endTime="39.087 ">\n',  # 13
    u'<Sync time=" 32.282"/>\n',                                      # 14
    u'오, 그렇다면 나는 랜덤 캐릭터. [noise]\n',                        # 15
    u'</Turn>\n',                                                     # 16
    u'<Turn speaker="spk5 " startTime="39.087" endTime="43.950">\n',  # 17
    u'<Sync time="39.087 "/>\n',                                      # 18
    u'아, 이 아저씨가 여기서 또 옷 벗고 있네? 따라와요.\n',              # 19
    u'</Turn>\n',                                                     # 20
    u'<Turn speaker=" spk1" startTime="43.950" endTime="58.756">\n',  # 21
    u'<Sync time= "43.950"/>\n',                                      # 22
    u'[overlap]\n',                                                   # 23
    u'</Turn>\n',                                                     # 24
    u'<Turn speaker= "spk6" startTime="58.756" endTime="68.486">\n',  # 25
    u'<Sync time ="58.756"/>\n',                                              # 26
    u'[music] 아하. [noise] 어, 우와. 내 머리는 길지만 니 수명을 짧을 거야.\n',  # 27
    u'</Turn>\n',                                                             # 28
    u'<Turn speaker="spk2" startTime="956.003" endTime="957.894">\n',         # 29
    u'<Sync time="59.003"/>\n',                                              # 30
    u'Thank you candidate Graham. [overlap] Thanks.\n',                       # 31
    u'</Turn>\n',                                                             # 32
    u'<Turn speaker ="spk4" startTime="68.486" endTime="73.614">\n',          # 33
    u'<Sync time="68.486"/>\n',                                               # 34
    u'[laugh] 그래. 그럼 나는 영화 어 아저씨의 멋있는 원빈! [noise]\n',          # 35
    u'</Turn>\n',                                                             # 36
    u'<Turn startTime ="3170.236" endTime="3171.857">\n',                      # 37
    u'<Sync time="3170.236"/>\n',                                             # 38
    u'[noise] &lt;lang:Foreign&gt;ČSSDspacing 5ČSSD &lt;/lang:Foreign&gt;\n', # 39
    u'</Turn>\n',                                                             # 40
    u'<Turn startTime= "3170.236" endTime="3171.857">\n',                     # 41
    u'<Turn startTime=" 3170.236" endTime="3171.857">\n',                     # 42
    u'<Turn startTime="3170.236 " endTime="3171.857">\n',                     # 43
    u'<Turn startTime ="3170.236" endTime="3171.857">\n',                     # 44
    u'<Turn startTime="3170.236" endTime= "3171.857">\n',                     # 45
    u'<Turn startTime="3170.236" endTime="3171.857" speaker="spk2 ">'         # 46
]


def test_command24(tmpdir):
    file_ = temporary_file(tmpdir, CONTENT)
    found = command24(file_)

    #for key in sorted(found.keys()):
        #print(key, found[key])

    assert 1 in found
    assert not 2 in found
    assert not 3 in found
    assert not 4 in found
    assert 5 in found
    assert 6 in found
    assert not 7 in found
    assert not 8 in found
    assert 9 in found
    assert 10 in found
    assert not 11 in found
    assert not 12 in found
    assert 13 in found
    assert 14 in found
    assert not 15 in found
    assert not 16 in found
    assert 17 in found
    assert 18 in found
    assert not 19 in found
    assert not 20 in found
    assert 21 in found
    assert 22 in found
    assert not 23 in found
    assert not 24 in found
    assert 25 in found
    assert 26 in found
    assert not 27 in found
    assert not 28 in found
    assert not 29 in found
    assert not 30 in found
    assert not 31 in found
    assert not 32 in found
    assert 33 in found
    assert not 34 in found
    assert not 35 in found
    assert not 36 in found
    assert 37 in found
    assert 38 in found
    assert not 39 in found
    assert not 40 in found
    assert 41 in found
    assert 42 in found
    assert 43 in found
    assert 44 in found
    assert 45 in found
    assert 46 in found

    #assert 0

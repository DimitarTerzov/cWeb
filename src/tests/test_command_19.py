# -*- coding: utf-8 -*-
from __future__ import print_function

from utils import temporary_file
from command_19.validator_19 import command19


CONTENT = [
    u'<Turn speaker="spk2" startTime="6.557" endTime="10.968">\n',         # 0
    u'<Sync time="6.557"/>\n',                                                                         # 1
    u"I'm not gonna comment on\n",                                                                  # 2
    u'<Sync time="9.557"/>\n',                                                                          # 3
    u"that. I'll get fined for the rest of my life if I could comment on that.\n",    # 4
    u'</Turn>\n',                                                                                                 # 5

    u'<Turn speaker="spk3" startTime="10.968" endTime="20.242">\n',    # 6
    u'<Sync time="10.968"/>\n',                                                                    # 7
    u"We had a great belief in our locker room. We didn't have to do \
    anything special, just be us.\n",                                                                 # 8
    u'<Sync time="15.968"/>\n',                                                                    # 9
    u"I was so proud of this team. We had so much fun, \
    it all ought to be illegal.\n",                                                                       # 10
    u'</Turn>\n',                                                                                             # 11

    u'<Turn speaker="spk4" startTime="20.242" endTime="23.808">\n',    # 12
    u'<Sync time="20.242"/>\n',                                                                     # 13
    u'Coach (()) is that something you just,\n',                                                 # 14
    u'<Sync time="21.242"/>\n',                                                                     # 15
    u'see?\n',                                                                                                     # 16
    u'</Turn>\n',                                                                                               # 17

    u'<Turn speaker="spk5" startTime="23.808" endTime="57.808">\n',    # 18
    u'<Sync time="23.808"/>\n',                                                                     # 19
    u"Yeah, yeah, yeah you ignore it cause one week you're getting\n",         # 20
    u'<Sync time="27.808"/>\n',                                                                     # 21
    u"fired, the next week you're gonna answer your question\n",                  # 22
    u'<Sync time="29.808"/>\n',                                                                     # 23
    u"fired? The next week you're gonna\n",                                                    # 24
    u'<Sync time="32.808"/>\n',                                                                     # 25
    u"fired! the next week you're gonna\n",                                                     # 26
    u'<Sync time="35.808"/>\n',                                                                     # 27
    u"\n",                                                                                                          # 28
    u'<Sync time="37.808"/>\n',                                                                     # 29
    u"fired. the next week you're gonna\n",                                                     # 30
    u'<Sync time=" 50.808"/>\n',                                                                    # 31
    u"fired. the next week you're gonna.\n",                                                     # 32
    u'<Sync time=" 55.808"/>\n',                                                                    # 33
    u"\n",                                                                                                           # 34
    u'<Sync time=" 57.808"/>\n',                                                                    # 35
    u"The next week you're gonna.\n",                                                             # 36
    u'</Turn>\n',                                                                                              # 37
    
    u'<Turn speaker="spk4" startTime="20.242" endTime="23.808">\n',     # 38
    u'<Sync time="20.242"/>\n',                                                                     # 39
    u'Coach (()) is that something you just\n',                                                  # 40
    u'<Sync time="21.242"/>\n',                                                                     # 41
    u'can\'t see? Blah Blah blah.\n',                                                                  # 42
    u'</Turn>\n',                                                                                              # 43
    
    u'<Turn speaker="spk5" startTime="23.808" endTime="57.808">\n',    # 44
    u'<Sync time="23.808"/>\n',                                                                     # 45
    u"Yeah, yeah, yeah you ignore it cause one week you're. Getting\n",         # 46
    u'<Sync time="33.808"/>\n',                                                                     # 47
    u"fired, the next week you're gonna answer your question.\n",                  # 48
    u'<Sync time="39.808"/>\n',                                                                     # 49
    u"Fired the next week you're gonna.\n",                                                    # 50
    u'</Turn>\n',                                                                                              # 51
]
EXCLUDES = [
    0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11,
    12, 13, 14, 15, 16, 17, 18, 19,
    20, 21, 22, 23, 25, 27, 28, 29,
    31, 32, 33, 34, 35, 36, 37, 38,
    39, 40, 41, 42, 43, 44, 45, 47,
    49, 50, 51
]
CATCH = [4, 24, 26, 30, 46, 48]


def test_command_19(monkeypatch, tmpdir):
    file_ = temporary_file(tmpdir, CONTENT)
    found = command19(file_)

    for key in sorted(found.keys()):
        print(key, found[key])

    for item in EXCLUDES:
        assert item not in found

    for item in CATCH:
        assert item in found

    assert 0

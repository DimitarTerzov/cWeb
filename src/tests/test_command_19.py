# -*- coding: utf-8 -*-
from __future__ import print_function

from utils import temporary_file
from command_19.validator_19 import command19


CONTENT = [
    u'<Turn speaker="spk2" startTime="6.557" endTime="10.968">\n',         # 1
    u'<Sync time="6.557"/>\n',                                                                         # 2
    u"I'm not gonna comment on\n",                                                                  # 3
    u'<Sync time="9.557"/>\n',                                                                          # 4
    u"that. I'll get fined for the rest of my life if I could comment on that.\n",    # 5
    u'</Turn>\n',                                                                                                 # 6

    u'<Turn speaker="spk3" startTime="10.968" endTime="20.242">\n',    # 7
    u'<Sync time="10.968"/>\n',                                                                    # 8
    u"We had a great belief in our locker room. We didn't have to do \
    anything special, just be us.\n",                                                                 # 9
    u'<Sync time="15.968"/>\n',                                                                    # 10
    u"I was so proud of this team. We had so much fun, \
    it all ought to be illegal.\n",                                                                       # 11
    u'</Turn>\n',                                                                                             # 12

    u'<Turn speaker="spk4" startTime="20.242" endTime="23.808">\n',    # 13
    u'<Sync time="20.242"/>\n',                                                                     # 14
    u'Coach (()) is that something you just,\n',                                                 # 15
    u'<Sync time="21.242"/>\n',                                                                     # 16
    u'see?\n',                                                                                                     # 17
    u'</Turn>\n',                                                                                               # 18

    u'<Turn speaker="spk5" startTime="23.808" endTime="57.808">\n',    # 19
    u'<Sync time="23.808"/>\n',                                                                     # 20
    u"Yeah, yeah, yeah you ignore it cause one week you're getting\n",         # 21
    u'<Sync time="27.808"/>\n',                                                                     # 22
    u"fired, the next week you're gonna answer your question\n",                  # 23
    u'<Sync time="29.808"/>\n',                                                                     # 24
    u"fired? The next week you're gonna\n",                                                    # 25
    u'<Sync time="32.808"/>\n',                                                                     # 26
    u"fired! the next week you're gonna\n",                                                     # 27
    u'<Sync time="35.808"/>\n',                                                                     # 28
    u"\n",                                                                                                          # 29
    u'<Sync time="37.808"/>\n',                                                                     # 30
    u"fired. the next week you're gonna\n",                                                     # 31
    u'<Sync time=" 50.808"/>\n',                                                                    # 32
    u"fired. the next week you're gonna.\n",                                                     # 33
    u'<Sync time=" 55.808"/>\n',                                                                    # 34
    u"\n",                                                                                                           # 35
    u'<Sync time=" 57.808"/>\n',                                                                    # 36
    u"The next week you're gonna.\n",                                                             # 37
    u'</Turn>\n',                                                                                              # 38

    u'<Turn speaker="spk4" startTime="20.242" endTime="23.808">\n',     # 39
    u'<Sync time="20.242"/>\n',                                                                     # 40
    u'Coach (()) is that something you just\n',                                                  # 41
    u'<Sync time="21.242"/>\n',                                                                     # 42
    u'can\'t see? Blah Blah blah.\n',                                                                  # 43
    u'</Turn>\n',                                                                                              # 44

    u'<Turn speaker="spk5" startTime="23.808" endTime="57.808">\n',    # 45
    u'<Sync time="23.808"/>\n',                                                                    # 46
    u"Yeah, yeah, yeah you ignore it cause one week you're. Getting\n",      # 47
    u'<Sync time="33.808"/>\n',                                                                   # 48
    u"fired, the next week you're gonna answer your question.\n",  # 49
    u'<Sync time="39.808"/>\n',                                                                   # 50
    u'některé\n',                                                                                              # 51
    u'scény nezapomněli doteď.\n',                                                                 # 52
    u'<Sync time="42.808"/>\n',                                                                    # 53
    u"Yeah, yeah, yeah you ignore it cause one week you're. [music] \n",      # 54
    u'<Sync time="43.808"/>\n',                                                                   # 55
    u"fired, the next week you're gonna answer your question.\n",               # 56
    u'</Turn>\n',                                                                                             # 57
    u'<Turn speaker="spk1" startTime="5.195" endTime="6.557">\n',       # 58
    u'<Sync time="5.195"/>\n',                                                                     # 59
    u'When the replay official. Did wrong\n',                                                  # 60
    u'<Sync time="6.557"/>\n',                                                                     # 61
    u"i'm not gonna comment on that. I'll get fined for the rest of my life if I could comment.\n",         # 62
    u'<Sync time="10.968"/>\n',                                                                                                            # 63
    u"We had a great belief in our locker room. We didn't have to do anything special, just be us. \n",# 64
    u'<Sync time="20.242"/>\n',                                                                                                            # 65
    u'Coach (()) is that something you just ignore\n',                                                                             # 66
    u'<Sync time="23.808"/>\n',                                                                                                           # 67
    u"yeah, yeah. Yeah you ignore it cause one week you're getting fired. \n",                                     # 68
    u'</Turn>    \n',                                                                                                                                 # 69
]
EXCLUDES = [
    1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12,
    13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 26, 28, 29, 30,
    32, 33, 34, 35, 36, 37, 38, 39,
    40, 41, 42, 44, 45, 46, 48,
    49, 50, 51, 52, 53, 54, 55, 56,
    57, 58, 59, 61, 62, 63, 64, 65,
    66, 67, 69
]
CATCH = [5, 25, 27, 31, 43, 47, 60, 68]


def test_command_19(tmpdir):
    file_ = temporary_file(tmpdir, CONTENT)
    found = command19(file_)

    for key in sorted(found.keys()):
        print(key, found[key])

    for item in EXCLUDES:
        assert item not in found

    for item in CATCH:
        assert item in found

    assert 0

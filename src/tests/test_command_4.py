# -*- coding: utf-8 -*-
from __future__ import print_function

import pytest

from utils import temporary_file
from command_4.validator_4 import command4


CONTENT = [
    u"&lt;initial&gt; error1 &lt;/initial&gt;&gt; Good evening once again.\n",            # 0
    u"<initial> error2 </initial>  And we're here to once again\n",                       # 1
    u"&lt;initial&gt; error3 &lt;initial&gt; Who have demonstrated that #uh,\n",          # 2
    u"For the &lt;initial&gt; W. E. B. &lt;/initial&gt; Du Bois.\n",                      # 3
    u"&lt;initial&gt; error4 &lt;/Initial&gt; So once again,\n",                          # 4
    u"(music) &lt;initial&gt; error5 &lt; /initial&gt;\n",                                # 5
    u"Thank you, Paul. &lt; initial&gt; error6 &lt;/initial&gt;\n",                       # 6
    u"[no-speech] &lt;initial&gt; error7 &lt;/iniial&gt;\n",                              # 7
    u"&lt;initial&gt; error8&lt;/initial&gt; My name is Julia Novena,\n",                 # 8
    u"We are going to again, uh, or George &lt;initial&gt; W. &lt;/initial&gt; Bush.\n",  # 9
    u"[noise] &lt;initial&gt;error9 &lt;/initial&gt;\n",                                  # 10
    u"Thank you. &lt;/initial&gt; error10 &lt;/initial&gt;\n",                            # 11
    u"[noise]  &lt;initial&gt; error 11 &lt;/initial&gt;\n",                              # 12
    u"[no-speech]  &lt;&lt;initial&gt; error12 &lt;/initial&gt;\n",                       # 13
    u"&lt;initial&gt; error 13 &lt;/initial &gt; In a meaningful way.\n",                 # 14
    u"It is not good enough &lt;initial&gt;error14&lt;/initial&gt; to just go\n",         # 15
    u"We must add, we must &lt;initial&gt; W! E. B. &lt;/initial&gt;\n",                  # 16
    u"The vote that we cast are &lt;initial&gt; W E B &lt;/initial&gt; important.\n",     # 17
    u"For two years, municipal, &lt;initial&gt; W?EB &lt;/initial&gt;\n",                 # 18
    u"The decision to vote always &lt;initial&gt; W! &lt;/initial&gt;\n",                 # 19
    u"This is why we &lt;initialism&gt; ČSSD &lt;/initialism&gt;\n",                       # 20
    u"between the &lt;initial&gt; PTO &lt;/initial&gt;'s\n",                              # 21
    u"by the &lt;initial&gt; FDA &lt;/initial&gt; and\n",                                 # 22
    u"Pre &lt;initial&gt; K &lt;/initial&gt; through twelveth grade.\n",                  # 23
    u"&lt;initial&gt; MHS &lt;/initial&gt;, I was a student\n",                           # 24
    u"&lt;initial&gt; PTO &lt;/initial&gt;s for the enrichment\n",                        # 25
    u"I attended &lt;initial&gt; ČSSD &lt;/initial&gt;.\n",                                # 26
    u"I attended &lt;initial&gt; ČSSD, ČSSD &lt;/initial&gt;.\n",                           # 27
    u"French l'&lt;initial&gt; ONU &lt;/initial&gt;\n",                                   # 28
    u"This one is correct... &lt;initial&gt; Ph.D. &lt;/initial&gt;\n"                    # 29
    u"between the &lt;initial&gt; PTO &lt;/initial&gt;o\n",                               # 30
    u'&lt;initial&gt; AY &lt;/initial&gt;-liikkeen\n',                                    # 31
    u'&lt;initial&gt; AY &lt;/initial&gt;!liikkeen\n',                                    # 32
    u'&lt;initial&gt; AY &lt;/initial&gt;?liikkeen\n',                                    # 33
    u'&lt;initial&gt; AY &lt;/initial&gt;:liikkeen\n',                                    # 34
    u'&lt;initial&gt; AY &lt;/initial&gt;;liikkeen\n',                                    # 35
    u'&lt;initial&gt; AY &lt;/initial&gt;_liikkeen\n',                                    # 36
    u'&lt;initial&gt; AY &lt;/initial&gt;—liikkeen\n',                                   # 37
    u'Ремонтират улица <initial>Богориди<initial>.\n',                       # 38
    u'&lt;initial&gt; AY &lt;/initial&gt;~ \n',                                                # 39
    u"French &lt;initial&gt; ONU &lt;/initial&gt;n\n",                                  # 40
    u"French &lt;initial&gt; ONU &lt;/initial&gt;sn\n",                                 # 41
    u'&lt;initial&gt;\n',                                                                                 # 42
    u'mais plutôt en termes &lt;/initial&gt;\n',                                            # 43
]


def test_command4(tmpdir):
    file_ = temporary_file(tmpdir, CONTENT)
    found = command4(file_)

    keys = sorted(found.keys())
    print(len(keys))
    for key in keys:
        print(key, found[key])

    assert 0 in found
    assert 1 not in found
    assert 2 in found
    assert not 3 in found
    assert 4 in found
    assert 5 in found
    assert 6 in found
    assert 7 in found
    assert 8 in found
    assert not 9 in found
    assert 10 in found
    assert 11 in found
    assert 12 in found
    assert 13 in found
    assert 14 in found
    assert 15 in found
    assert 16 in found
    assert 17 in found
    assert 18 in found
    assert 19 in found
    assert 20 in found
    assert not 21 in found
    assert not 22 in found
    assert not 23 in found
    assert not 24 in found
    assert not 25 in found
    assert not 26 in found
    assert 27 in found
    assert 28 in found
    assert not 29 in found
    assert 30 in found
    assert 31 not in found
    assert 32 not in found
    assert 33 not in found
    assert 34 not in found
    assert 35 not in found
    assert 36 not in found
    assert 37 not in found
    assert 38 not in found
    assert 39 not in found
    assert 40 in found
    assert 41 in found
    assert 42 in found
    assert 43 in found

    #assert 0

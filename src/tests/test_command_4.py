from __future__ import print_function

import pytest

from utils import temporary_file
from command_4.validator_4 import command4


CONTENT = [
    "&lt;initial&gt; error1 &lt;/initial&gt;&gt; Good evening once again.\n",            # 0
    "<initial> error2 </initial>  And we're here to once again\n",                       # 1
    "&lt;initial&gt; error3 &lt;initial&gt; Who have demonstrated that #uh,\n",          # 2
    "For the &lt;initial&gt; W. E. B. &lt;/initial&gt; Du Bois.\n",                      # 3
    "&lt;initial&gt; error4 &lt;/Initial&gt; So once again,\n",                          # 4
    "(music) &lt;initial&gt; error5 &lt; /initial&gt;\n",                                # 5
    "Thank you, Paul. &lt; initial&gt; error6 &lt;/initial&gt;\n",                       # 6
    "[no-speech] &lt;initial&gt; error7 &lt;/iniial&gt;\n",                              # 7
    "&lt;initial&gt; error8&lt;/initial&gt; My name is Julia Novena,\n",                 # 8
    "We are going to again, uh, or George &lt;initial&gt; W. &lt;/initial&gt; Bush.\n",  # 9
    "[noise] &lt;initial&gt;error9 &lt;/initial&gt;\n",                                  # 10
    "Thank you. &lt;/initial&gt; error10 &lt;/initial&gt;\n",                            # 11
    "[noise]  &lt;initial&gt; error 11 &lt;/initial&gt;\n",                              # 12
    "[no-speech]  &lt;&lt;initial&gt; error12 &lt;/initial&gt;\n",                       # 13
    "&lt;initial&gt; error 13 &lt;/initial &gt; In a meaningful way.\n",                 # 14
    "It is not good enough &lt;initial&gt;error14&lt;/initial&gt; to just go\n",         # 15
    "We must add, we must &lt;initial&gt; W! E. B. &lt;/initial&gt;\n",                  # 16
    "The vote that we cast are &lt;initial&gt; W E B &lt;/initial&gt; important.\n",     # 17
    "For two years, municipal, &lt;initial&gt; W?EB &lt;/initial&gt;\n",                 # 18
    "The decision to vote always &lt;initial&gt; W! &lt;/initial&gt;\n",                 # 19
    "This is why we &lt;initialism&gt; WER &lt;/initialism&gt;\n",                       # 20
    "between the &lt;initial&gt; PTO &lt;/initial&gt;'s\n",                              # 21
    "by the &lt;initial&gt; FDA &lt;/initial&gt; and\n",                                 # 22
    "Pre &lt;initial&gt; K &lt;/initial&gt; through twelveth grade.\n",                  # 23
    "&lt;initial&gt; MHS &lt;/initial&gt;, I was a student\n",                           # 24
    "&lt;initial&gt; PTO &lt;/initial&gt;s for the enrichment\n",                        # 25
    "I attended &lt;initial&gt; MHS &lt;/initial&gt;.\n",                                # 26
    "I attended &lt;initial&gt; FBI, CIA &lt;/initial&gt;.\n",                           # 27
    "French l'&lt;initial&gt; ONU &lt;/initial&gt;\n",                                   # 28
    "This one is correct... &lt;initial&gt; Ph.D. &lt;/initial&gt;\n"                    # 29
    "between the &lt;initial&gt; PTO &lt;/initial&gt;o"                                  # 30
]


def test_command4(tmpdir):
    file_ = temporary_file(tmpdir, CONTENT)
    found = command4(file_)

    #keys = sorted(found.keys())
    #print(len(keys))
    #for key in keys:
        #print(key, found[key])

    assert 0 in found
    assert 1 in found
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
    assert not 28 in found
    assert not 29 in found
    assert 30 in found

    #assert 0
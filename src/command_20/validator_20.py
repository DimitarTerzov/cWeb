# -*- coding: utf-8 -*-
from __future__ import print_function

import re
import io


def command20(filepath):
    disallowed_punctuation = re.compile(ur"<.*?>", re.UNICODE)

    found = {}
    with io.open (filepath, 'r', encoding='utf') as f:
        ln = 0
        sync = False
        for line in f:
            line = line.strip()

            if line.startswith(u'<Sync'):
                sync = True

            elif sync and not line == u'</Turn>':
                match = re.search(disallowed_punctuation, line)
                if match is not  None:
                    found[ln] = [20, 'Disallowed punctuation', match.group().encode('utf')]
                sync = False

            else:
                sync = False

            ln += 1

    return found


if __name__ == '__main__':
    found = command20('../files/test_5.trs')
    for key in sorted(found.keys()):
        print(key, found[key])

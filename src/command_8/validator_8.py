# -*- coding: utf-8 -*-
from __future__ import print_function

import re
import io


#White space validator
def command8(filepath):
    rv = {}
    patterns = [ur'\[.*?\]',  ur'\(\(\)\)', ur'\(\(.*?\)\)']

    for pat in patterns:
        found = command8_real(filepath, pat)
        rv.update(found)
    return rv


def command8_real(filepath, pattern):

    reg_allowed = u',。！？，、．\[\]\w;&#\(\)'
    regex_pat = ur'(.?){}(.?)'.format(pattern)

    found = {}
    with io.open(filepath, 'r', encoding='utf') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")
            line = line.strip()

            #if line starts with < and ends in >
            if line.startswith('<') and line.endswith('>'):
                #we skip everythin between <>
                continue

            # Skip <lang> and <initial> tags.
            if re.search(ur'(&gt;|>)\s*?{}\s*?(&lt;|<)'.format(pattern), line, re.UNICODE) is not None:
                continue

            for m in re.finditer(regex_pat, line):
                content = m.group()
                lC = m.group(1)
                rC = m.group(2)

                if lC and re.match(ur'[{}]'.format(reg_allowed), lC, re.UNICODE) is None:
                    found[ln] =  [8, 'Incorrect white space (invalid left char)', '{}/{}'.format(lC.encode('utf'), content.encode('utf'))]

                elif rC and re.match(ur'[{}]'.format(reg_allowed), rC, re.UNICODE) is None:
                    found[ln] =  [8, 'Incorrect white space (invalid right char)', '{}/{}'.format(rC.encode('utf'), content.encode('utf'))]

                elif pattern == u'\[.*?\]' and re.search(ur'\[[\w-]*?\]', content, re.UNICODE) is None:
                    found[ln] =  [8, 'Incorrect white space in tag', content.encode('utf')]

                elif pattern == u'\(\(.*?\)\)' and re.search(ur'\(\([\w\-{}]*?\)\)'.format(reg_allowed), content, re.UNICODE) is None:
                    found[ln] =  [8, 'Incorrect white space in tag', content.encode('utf')]

    return found


if __name__ == "__main__":
    found = command8('../files/TTV_FuPeimeiTime_025.trs')
    for key in sorted(found.keys()):
        print(key, found[key])

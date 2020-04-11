# -*- coding: utf-8 -*-
from __future__ import print_function
import re
import io


#Punctuation space validator
def command11(filepath):

    exlusion_list = ['-nya', '-exclusion2', '-exclusion3']

    #match a symbol with one space
    regex = re.compile(ur'(\s\-\s)|(\s[\.,，。!?-])|([\.,，。!?-]\s{3,})|([\.,，。!?][^\s])', re.UNICODE)

    found = {}

    with io.open(filepath, 'r', encoding='utf') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip(" \r\n")

            #if line starts with < and ends in >
            if line.startswith('<') and line.endswith('>'):
                #we skip everythin between <>
                continue

            for m in re.findall(regex, line):

                val = exlusion_list[0]

                #allow ' - '
                if m[0]:
                    val = exlusion_list[0]
                elif m[1]:
                    val = m[0]
                elif m[2]:
                    val = m[1]
                elif m[3]:
                    val = ''

                if not val in exlusion_list:
                    found[ln] = [11, 'Punctuation spacing issue', line.encode('utf')]

    return found


if __name__ == '__main__':
    found = command11('../files/tesst.trs')
    for key in sorted(found):
        print(key, found[key])

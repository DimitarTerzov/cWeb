# -*- coding: utf-8 -*-
from __future__ import print_function

import re
import io


# Code errors
def command24(filepath):

    inspect_sync_re = re.compile(ur'<(\s*)[Sync\w]+(?:\s*)[time\w]+(\s*)=(\s*)"(\s*)[\d\.]+(\s*)"/(\s*)>', re.UNICODE)
    inspect_turn_re = re.compile(ur'<[Turn\w]+(?:\s*[speaker\w]+(\s*)=(\s*)"(\s*)[spk\w]+\d+(\s*)")?\s*[startTime\w]+(\s*)=(\s*)"(\s*)[\d\.]+(\s*)"\s*[endTime\w]+(\s*)=(\s*)"(\s*)[\d\.]+(\s*)"(?:\s*[speaker\w]+(\s*)=(\s*)"(\s*)[spk\w]+\d+(\s*)")?>', re.UNICODE)

    found = {}

    with io.open(filepath, 'r', encoding='utf') as f:

        ln = 0
        for line in f:
            ln += 1
            line = line.rstrip("\r\n")

            match = re.match(inspect_sync_re, line)
            if match is not None:

                if re.search(ur'\bSync\b\s*\btime\b', line, re.UNICODE) is None:
                    found[ln] = [24, 'Tag syntax error', line.encode('utf')]
                    continue

                for group in match.groups():
                    if group is not None and group != "":
                        found[ln] = [24, 'Unexpected white space in Sync tag', line.encode('utf')]
                        break

                continue

            match = re.match(inspect_turn_re, line)
            if match is not None:

                if re.search(ur'\bTurn\b.*?\bstartTime\b.*?\bendTime\b.*?>', line, re.UNICODE) is None:
                    found[ln] = [24, 'Tag syntax error', line.encode('utf')]
                    continue

                for group in match.groups():
                    if group is not None and group != "":
                        found[ln] = [24, 'Unexpected white space in Turn tag', line.encode('utf')]
                        break

                continue

            if u'<Speaker' in line and line != '<Speakers>':
                if re.match(ur'<Speaker.*?/>', line, re.UNICODE) is None:
                    found[ln] = [24, 'Tag syntax error', line.encode('utf')]

    return found


if __name__ == '__main__':
    found = command24(r'../files/Ykkosaamu_007.trs')
    print(len(found))
    keys = sorted(found.keys())
    for key in keys:
        print(key, found[key])

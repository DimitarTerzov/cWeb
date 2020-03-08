# -*- coding: utf-8 -*-
from __future__ import print_function

import re


# Code errors
def command24(filepath):
    import io

    inspect_sync_re = re.compile(r'<(?P<s_1>\s*)Sync(?:\s*)time(?P<s_2>\s*)=(?P<s_3>\s*)"(?P<s_4>\s*)(?P<time>[\d\.]+)(?P<s_5>\s*)"/(?P<s_6>\s*)>', re.UNICODE)
    inspect_turn_re = re.compile(r'<Turn(?:\s*speaker(\s*)=(\s*)"(\s*)spk\d+(\s*)")?\s*startTime(\s*)=(\s*)"(\s*)[\d\.]+(\s*)"\s*endTime(\s*)=(\s*)"(\s*)[\d\.]+(\s*)"(?:\s*speaker(\s*)=(\s*)"(\s*)spk\d+(\s*)")?>', re.UNICODE)

    found = {}
    cur_time = 0

    with io.open(filepath, 'r', encoding='utf') as f:

        ln = 0
        for line in f:
            ln += 1
            line = line.rstrip("\r\n")

            match = re.match(inspect_sync_re, line)
            if match is not None:

                seg_time = float(match.group('time'))
                seg_len = seg_time - cur_time
                if seg_len > 15.0:
                    found[ln] = [24, 'Segment exceeds limit', 'Sync time="{}"; length: {} seconds'.format(seg_time, seg_len)]
                    cur_time = seg_time
                    continue

                elif (
                    match.group('s_1') or
                    match.group('s_2') or
                    match.group('s_3') or
                    match.group('s_4') or
                    match.group('s_5') or
                    match.group('s_6')
                ):
                    found[ln] = [24, 'Unexpected white space in Sync tag', line.encode('utf')]
                    cur_time = seg_time
                    continue

                #update current time
                cur_time = seg_time
                continue

            match = re.match(inspect_turn_re, line)
            if match is not None:
                for group in match.groups():
                    if group is not None and group != "":
                        found[ln] = [24, 'Unexpected white space in Turn tag', line.encode('utf')]
                        break

    return found


if __name__ == '__main__':
    found = command24(r'../files/KBS_Gag_Concert_2019_11_02.trs')
    print(len(found))
    keys = sorted(found.keys())
    for key in keys:
        print(key, found[key])

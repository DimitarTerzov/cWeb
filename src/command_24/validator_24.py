# -*- coding: utf-8 -*-
from __future__ import print_function

import re
import io


#Segment length validator
def command24(filepath):

    sync_time_value_re = re.compile('<Sync time="\s*([\d\.]+)\s*"/>', re.UNICODE)
    #regez = re.compile("<Sync time=\"" + WWwhitespace +"+[0-9\.]+\"/>|<Sync time=\"[0-9\.]+"+ WWwhitespace+"\"/>|<Sync time=\""+ WWwhitespace +"+[0-9\.]+"+ WWwhitespace+"\"/>")

    found = {}
    cur_time = 0

    with io.open(filepath, 'r', encoding='utf') as f:

        ln = 1
        for line in f:

            line = line.rstrip("\r\n")
            for m in re.findall(sync_time_value_re, line):

                seg_time = float(m)
                seg_len = seg_time - cur_time
                if seg_len > 15.0:
                    found[ln] = [24, 'Segment exceeds limit', 'Sync time="{}"; length: {} seconds'.format(seg_time, seg_len)]

                #update current time
                cur_time = seg_time

            ln += 1

            #for m in re.findall(regez, line):
                #found[ln] = [14, 'Unexpected white space in sync time tag', line]

    return found


if __name__ == '__main__':
    found = command24(r'../files/KBS_Gag_Concert_2019_11_02.trs')
    print(len(found))
    keys = sorted(found.keys())
    for key in keys:
        print(key, found[key])

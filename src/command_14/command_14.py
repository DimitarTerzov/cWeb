import re

from app.cWeb import WWwhitespace


#Segment length validator
def command14(filepath):

    regex = re.compile('<Sync time="\s*([0-9\.]+)\s*"/>')
    regez = re.compile("<Sync time=\"" + WWwhitespace +"+[0-9\.]+\"/>|<Sync time=\"[0-9\.]+"+ WWwhitespace+"\"/>|<Sync time=\""+ WWwhitespace +"+[0-9\.]+"+ WWwhitespace+"\"/>")

    found = {}
    cur_time = 0.0

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")
            for m in re.findall(regex, line):

                seg_time = float(m)
                seg_len = seg_time - cur_time

                if seg_len > 15.0:
                    found[ln] = [14, 'Segment exceeds limit', 'Sync time="' + str(cur_time) + '" length: ' + str(seg_len) + ' seconds']

                #update current time
                cur_time = seg_time
            for m in re.findall(regez, line):

                found[ln] = [14, 'Unexpected white space in sync time tag', line]


    return found


if __name__ == '__main__':
    #print(WWwhitespace)
    found = command14('RNZ_Insight_002.trs')
    print(found)



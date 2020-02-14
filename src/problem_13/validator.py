import re


#Speaker validator
def command13(filepath):

    # Edit ReGex to match speaker at the beginning and the end of the Turn tag.
    regex = re.compile('<Turn (?:speaker="(spk[0-9]+)")?(?:.*)startTime="([0-9.]+)"(?:.*) (?:speaker="(spk[0-9]+)")?')

    found = {}

    prev_spk='none'
    sync = False

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            if 'sync' in line.lower():
                sync = True
            else:
                if "</Turn>" == line and sync:
                    found[ln] = [13, "Empty turns are not allowed"]
                    sync = False
                else:
                    sync = False

            for m in re.findall(regex, line):
                # If turn is speakerless -> set speaker to 'none'.
                if m[0] == '' and m[2] == '':
                    speaker = 'none'
                else:
                    # If turn has speaker -> take it.
                    speaker = m[0] if m[0] != '' else m[2]

                    if speaker == prev_spk:
                        found[ln] = [13, 'Sequential turns by the same speaker', speaker + " at " + m[1]]

                #save speaker
                prev_spk = speaker

    return found


if __name__ == "__main__":

    found = command13('RNZ_Insight_002.trs')
    for key, value in found.iteritems():
        print key, '; ', value

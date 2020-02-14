import re


SEQ_FILE_PATH = "sequential.trs"
NO_SEQ_FILE_PATH = "no_sequential.trs"
WORKING_FILE = "MedfordSchoolCommitteeCandid_2019.trs"


#Speaker validator
def command13(filepath):

    # Edit ReGex to match speaker at the beginning and the end of the Turn tag.
    regex = re.compile('<Turn (?:speaker="(spk[0-9]+)")?(?:.*)startTime="([0-9.]+)"(?:.*) (?:speaker="(spk[0-9]+)")?')

    found = {}

    prev_spk='none'

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")
            for m in re.findall(regex, line):
                # If turn is speakerless - set speaker to 'none'.
                if m[0] == '' and m[2] == '':
                    speaker = 'none'
                else:
                    # If turn has speaker - take it.
                    speaker = m[0] if m[0] != '' else m[2]

                if speaker == prev_spk:
                    found[ln] = [13, 'Sequential turns by the same speaker', speaker + " at " + m[1]]

                #save speaker
                prev_spk = speaker

    return found


if __name__ == "__main__":
    print(command13(SEQ_FILE_PATH))
    print(command13(NO_SEQ_FILE_PATH))
    print(command13(WORKING_FILE))

import re


#Speaker validator
def command13(filepath):

    regex = re.compile('<Turn (?:speaker="(spk[0-9]+)")?(?:.*)startTime="([0-9.]+)"(?:.*) (?:speaker="(spk[0-9]+)")?')

    found = {}

    prev_spk='none'
    sync = False
    sync_count = 0
    end_time = 0

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            # Catch empty turns and empty segments.
            if line == '':
                pass
            elif '<Turn' in line:
                start_time = re.search(r'(?P<content>startTime="(?P<value>\d+\.?\d*)")', line)
                start_value = float(start_time.group('value'))
                start_time = start_time.group('content')

                # Catch turns out of order
                if start_value != end_time:
                    found[ln] = [13, "Turn out of chronological order", start_time]

                end_time = re.search(r'endTime="(?P<value>\d+\.?\d*)"', line)
                end_time = float(end_time.group('value'))

            elif 'Sync' in line and not sync:
                sync = True
                sync_count += 1
                sync_time = re.search(r'(Sync time="\d+\.?\d*")', line)
                sync_time = sync_time.group()

            elif "</Turn>" == line and sync and sync_count == 1:
                found[ln] = [13, "Empty turns are not allowed", start_time]
                sync = False
                sync_count = 0

            elif 'Sync' in line and sync:
                found[ln] = [13, "Empty segments are not allowed", sync_time]
                sync_count += 1
                sync_time = re.search(r'(Sync time="\d+\.?\d*")', line)
                sync_time = sync_time.group()

            elif 'Sync' not in line and line != "</Turn>":
                sync = False

            elif "</Turn>" == line and sync and sync_count > 1:
                found[ln] = [13, "Empty segments are not allowed", sync_time]
                sync = False
                sync_count = 0

            elif "</Turn>" == line and not sync:
                sync = False
                sync_count = 0

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

    found = command13('../files/test_13.trs')
    keys = found.keys()
    keys = sorted(keys)
    for key in keys:
        print key, '; ', found[key]

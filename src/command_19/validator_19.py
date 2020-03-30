# -*- coding: utf-8 -*-
from __future__ import print_function
import re
import io


# Choppy segments
def command19(filepath):
    partial_line_end_marks = u":,\-_!—.?;"
    line_end_marks = u'!.?'
    turn_end = re.compile(ur'<\s*/\s*Turn\s*>', re.UNICODE)

    found = {}
    with io.open(filepath, 'r', encoding='utf') as f:

        ln = 0
        sync_time = None
        segment_lenght = 0
        in_turn = False
        check_for_choppy = False
        for line in f:
            line = line.rstrip("\r\n")

            if not line:
                ln += 1
                continue

            if re.search(ur'<\s*Turn', line, re.UNICODE) is not None:
                start_time = re.search(ur'startTime\s*=\s*"\s*(?P<value>[\d.]+?)\s*"', line, re.UNICODE)
                sync_time = float(start_time.group('value'))
                in_turn = True

            elif in_turn and re.search(ur'<\s*Sync\s*time', line, re.UNICODE) is not None:
                new_sync_time = re.search(ur'<\s*Sync\s*time\s*=\s*"\s*(?P<value>[\d.]+?)\s*"', line, re.UNICODE).group('value')
                new_sync_time = float(new_sync_time)
                segment_lenght = new_sync_time - sync_time
                sync_time = new_sync_time

            elif in_turn and re.search(turn_end, line) is None:

                if check_for_choppy and segment_lenght <= 12:
                    chopped = line.split()[0]
                    if (
                        len(chopped[: -1]) <= 5 and
                        re.search(ur'[{}]$'.format(line_end_marks), chopped, re.UNICODE) is not None and
                        chopped[0].islower()
                    ):
                        found[ln] = [19, "Choppy segment", line.encode('utf')]

                if (
                    re.search(ur'[{}]$'.format(partial_line_end_marks), line, re.UNICODE) is None
                ):
                    check_for_choppy = True
                else:
                    check_for_choppy = False

            elif re.search(turn_end, line) is not None:
                sync_time = None
                in_turn = False
                check_for_choppy = False

            ln += 1

    return found


if __name__ == '__main__':
    found = command19('../files/CT_Newsevents_40.trs')
    for key in sorted(found.keys()):
        print(key, found[key])

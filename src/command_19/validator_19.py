# -*- coding: utf-8 -*-
from __future__ import print_function
import re
import io


# Choppy segments
def command19(filepath):
    # Segments shorter than that amount of time in seconds
    # are potentially Chopped segments. You can control it
    # by changing this value.
    time_amount_left = 12    # Y
    # Segments that contain that number of words at the beginning
    # or at end are potentially Chopped segments. You can control
    # this by changing the value of variable.
    number_of_words = 2     # X

    partial_line_end_marks = u":,\-_!—.?;\]"
    line_end_marks = u'!.?'
    turn_end = re.compile(ur'<\s*/\s*Turn\s*>', re.UNICODE)

    found = {}
    with io.open(filepath, 'r', encoding='utf') as f:

        ln = 1
        sync_time = None
        segment_lenght = None
        in_turn = False
        check_for_choppy = False
        for line in f:
            line = line.rstrip(" \r\n")

            if not line:
                ln += 1
                continue

            if re.search(ur'<\s*Turn', line, re.UNICODE) is not None:
                sync_time = None
                segment_lenght = None
                chopped_at_end = False
                chopped_line_end = None
                check_for_choppy = False
                in_turn = True

            elif in_turn:

                if re.search(ur'<\s*Sync\s*time', line, re.UNICODE) is not None:

                    new_sync_time = re.search(ur'<\s*Sync\s*time\s*=\s*"\s*(?P<value>[\d.]+?)\s*"', line, re.UNICODE).group('value')
                    new_sync_time = float(new_sync_time)
                    if sync_time is not None:
                        segment_lenght = new_sync_time - sync_time

                    sync_time = new_sync_time
                    in_sync = True

                elif in_sync:

                    if check_for_choppy and segment_lenght <= time_amount_left:

                        for index in xrange(number_of_words):
                            try:
                                chopped = line.split()[index]
                            except IndexError:
                                pass
                            else:
                                if (
                                    re.search(ur'[{}]$'.format(line_end_marks), chopped, re.UNICODE) is not None and
                                    chopped[0].islower()
                                ):
                                    found[ln] = [19, "Choppy segment", line.encode('utf')]
                                    break

                    if chopped_at_end and segment_lenght <= time_amount_left and line[0].islower():
                        found[ln-2] = [19, "Choppy segment", chopped_line_end.encode('utf')]

                    if re.search(ur'[{}]$'.format(partial_line_end_marks), line, re.UNICODE) is None:

                        for index in xrange(-(number_of_words + 1), -1):
                            try:
                                chopped = line.split()[index]
                            except IndexError:
                                check_for_choppy = False
                                chopped_at_end = False
                                chopped_line_end = None
                            else:
                                if re.search(ur'[{}]$'.format(line_end_marks), chopped, re.UNICODE) is not None:
                                    chopped_at_end = True
                                    chopped_line_end = line
                                    break

                        check_for_choppy = True

                    else:
                        check_for_choppy = False
                        chopped_at_end = False
                        chopped_line_end = None

                    in_sync = False

            elif re.search(turn_end, line) is not None:
                in_turn = False

            ln += 1

    return found


if __name__ == '__main__':
    found = command19('../files/Ykkosaamu_007.trs')
    for key in sorted(found.keys()):
        print(key, found[key])

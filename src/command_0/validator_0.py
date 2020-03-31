# -*- coding: utf-8 -*-
from __future__ import print_function
import re
import io


LANGUAGE_CODES = {
    u'bul': u'Bulgarian',
    u'eng': u'English',
    u'ell': u'Greek'
}


# Transcribers validator
def command0(filepath):
    transcriber_pattern = re.compile(ur'\s*<\s*Trans\s*scribe\s*=.*?(?P<scriber>\w+?\-\d\d\d)\s*"', re.UNICODE)

    found = {}
    with io.open(filepath, 'r', encoding='utf') as f:
        ln = 0
        for line in f:
            line = line.rstrip('\r\n')

            if re.search(ur'\s*<\s*Trans\s*scribe\s*=', line, re.UNICODE) is not None:

                match = re.search(transcriber_pattern, line)
                if match is not None:

                    language_code = match.group('scriber')[:-4]
                    if language_code in LANGUAGE_CODES:
                        found['transcriber_id'] = match.group('scriber')
                    else:
                        found[ln] = [0, 'Incorrect Transcriber ID', line.encode('utf')]

                else:
                    found[ln] = [0, 'Incorrect Transcriber ID', line.encode('utf')]

                break

            ln += 1

    return found


if __name__ == '__main__':
    found = command0('')

# -*- coding: utf-8 -*-
from __future__ import print_function
import re
import io


#Sound tag validator
def command3(filepath):
    skip_words = [
        u'[no-speech]', u'[no—speech]', u'[noise]',
        u'[overlap]', u'[music]', u'[applause]',
        u'[lipsmack]', u'[breath]', u'[cough]',
        u'[laugh]', u'[click]', u'[ring]',
        u'[dtmf]', u'[sta]', u'[cry]', u'[prompt]'
    ]

    regex = re.compile(ur"\[.*?\]", re.UNICODE)

    found = {}
    tag_exists = False
    with io.open(filepath, 'r', encoding='utf') as f:
        ln = -1
        in_section = False
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            if '<Section' in line:
                in_section = True

            if in_section:
                for m in re.findall(regex, line):

                    if not m in skip_words:
                        found[ln] = [3, 'Sound tag syntax', '{}/{}'.format(m.encode('utf'), line.encode('utf'))]

                    # detect duplicate tags like - [cough] [cough]
                    # if we have two of the same tags in a row
                    # and they are one by one in the line
                    elif (
                        re.search(ur'{0}{0}'.format(re.escape(m)), line, re.UNICODE) is not None
                    ):
                        found[ln] = [3, 'Sound tag duplicate', '{}/{}'.format(m.encode('utf'), line.encode('utf'))]
                    tag_exists = True

    if not tag_exists and not found:
        found[1] = [3, 'No sound tag were found. Please refer to the project page to learn about the required use of sound tags.', '']

    return found


if __name__ == '__main__':
    found = command3('../files/CT_Newsevents_34.trs')
    for key in sorted(found.keys()):
        print(key, found[key])


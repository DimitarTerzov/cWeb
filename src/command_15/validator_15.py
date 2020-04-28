# -*- coding: utf-8 -*-
import re
import io


#Tilde checker
def command15(filepath):

    match_white_space = re.compile(ur'\w*(\s*)~(\s*)\w*', re.UNICODE)
    match_double_tilde = re.compile(ur'\W?.*?~~.*?\W', re.UNICODE)

    found = {}
    tag_exists = False
    in_section = False
    with io.open(filepath, 'r', encoding='utf') as f:
        ln = -1
        for line in f:
            ln = ln + 1

            if u'<Section' in line:
                in_section = True

            if in_section and u'~' in line:
                tag_exists = True

            if in_section:
                double_white_space = re.finditer(match_white_space, line)
                for match in double_white_space:
                    if match.group(1) or match.group(2):
                        found[ln] = [15, 'Incorrect white space', match.group(0).encode('utf')]

                double_tilde = re.findall(match_double_tilde, line)
                for match in double_tilde:
                    found[ln] = [15, 'Double tilde', match.encode('utf')]

    if not tag_exists and not found:
        found[1] = [15, 'No tildes were found. Please refer to the project page to learn about the proper use of the tilde for partially spoken words. If there were no partially spoken words, feel free to ignore this error.', '']

    return found


if __name__ == '__main__':
    found = command15('../files/no_tags.trs')
    for row, hit in found.items():
        print row, ' => ', hit

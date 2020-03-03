# -*- coding: utf-8 -*-
import re


#Filler word validator
def command7(filepath):

    # Allowed punctuation after tag
    punctuation = "[:',!—_\".?\-;]"
    #default english skip tags
    skip_tags = "(#uh|#um|#ah|#eh|#hm)"
    possible_missing_tag = "(uh|um|ah|eh|hm)"
    filler_re = re.compile(r'[\W\w]?#\w*\W?', re.UNICODE)

    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n").decode('utf')

            for match in re.finditer(filler_re, line):

                target = match.group().strip()
                # Pass filler tag with tilde.
                # They are reported in command 15.
                if "~" in target:
                    continue

                if not re.match(r'^{0}{1}?$'.format(skip_tags, punctuation), target, re.UNICODE):
                    found[ln] = [7, 'Invalid filler tag', match.group().encode('ascii', 'replace')]
                    continue


            for match in re.finditer(r'\s{0}\W'.format(possible_missing_tag), line, re.UNICODE):
                if ln not in found:
                    found[ln] = [7, 'Possible filler tag missing #', match.group().encode('ascii', 'replace')]

    return found


if __name__ == '__main__':
    found = command7()

# -*- coding: utf-8 -*-
import re


#Filler word validator
def command7(filepath):
    import io

    # Allowed punctuation after tag
    punctuation = u"[:',!—_\".?\-;]".encode('utf')
    #default skip tags
    skip_tags = u"(#uh|#um|#ah|#eh|#hm)".encode('utf')
    possible_missing_tag = u"(uh|um|ah|eh|hm)".encode('utf')
    filler_re = re.compile(r'[\W\w]?#\w*\W?', re.UNICODE)

    found = {}

    with io.open(filepath, 'r', encoding='utf') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            for match in re.finditer(filler_re, line):

                target = match.group().strip().encode('utf')
                # Pass filler tag with tilde.
                # They are reported in command 15.
                if "~" in target:
                    continue

                if not re.match(r'^{0}{1}?$'.format(skip_tags, punctuation), target, re.UNICODE):
                    found[ln] = [7, 'Invalid filler tag', target]
                    continue


            for match in re.finditer(r'\s{0}\W'.format(possible_missing_tag), line.encode('utf'), re.UNICODE):
                if ln not in found:
                    found[ln] = [7, 'Possible filler tag missing #', match.group()]

    return found


if __name__ == '__main__':
    found = command7("../files/Troldspejlet_20190620.trs")
    keys = sorted(found.keys())
    for key in keys:
        print key, found[key], found[key][2]

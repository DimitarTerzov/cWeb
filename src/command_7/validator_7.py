# -*- coding: utf-8 -*-
import re
import io


#Filler word validator
def command7(filepath):

    # Allowed punctuation after tag
    allowed_punctuation = ur"。！？，、．#\[\];.,\(\)"
    #default skip tags
    skip_tags = u"(#呃|#啊|#嗯)"
    filler_re = re.compile(ur'[\s\W\w]?#[\w\W]{,2}', re.UNICODE)

    found = {}
    in_section = False
    tag_exists = False
    with io.open(filepath, 'r', encoding='utf') as f:
        ln = 0
        for line in f:
            ln += 1
            line = line.rstrip("\r\n")

            if '<Section' in line:
                in_section = True
                continue

            if '</Section' in line:
                break

            if in_section:
                for match in re.finditer(filler_re, line):
                    tag_exists = True
                    target = match.group()
                    if (
                        re.match(ur'[\w{1}]?{0}[\w{1}]{2}$'.format(skip_tags, allowed_punctuation, '{,1}'), target, re.UNICODE) is None
                        ):
                        found[ln] = [7, 'Invalid filler tag', target.encode('utf')]

    if not tag_exists:
        found[1] = [7, 'No fillers tags were found. Please refer to the project page to learn about the required use of filler tags.', '']

    return found


if __name__ == '__main__':
    found = command7("../files/TTV_FuPeimeiTime_023.trs")
    keys = sorted(found.keys())
    for key in keys:
        print key, found[key], found[key][2]

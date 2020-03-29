# -*- coding: utf-8 -*-
from __future__ import print_function
import re
import io


def command19(filepath):
    #  WWwhitespacelist found in this file at: line 10
    regex = re.compile("&lt;initial&gt;\s*[a-zA-Z]+" + WWwhitespace + "+[a-zA-Z]+\s*&lt;\/initial&gt;")

    found = {}

    with open (filepath, 'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            for m in re.findall(regex, line):

                found[ln] = [19, 'Multiple initialisms in single tag', m]

    return found


if __name__ == '__main__':
    found = command19(filepath)
    for key in sorted(found.keys()):
        print(key, found[key])

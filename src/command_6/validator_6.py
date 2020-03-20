# -*- coding: utf-8 -*-
from __future__ import print_function

import re
import io


#Numeral hunter
def command6(filepath):

    found = {}

    with open(filepath) as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            #if line starts with < and ends in >
            if line.startswith('<') and line.endswith('>'):
                #we skip everythin between <>
                continue

            for word in line.split():
                if re.match('\S*\d+\S*', word) and not (word.startswith('<') and word.endswith('>')):
                    found[ln] = [6, 'Numerals not allowed', word]
    return found

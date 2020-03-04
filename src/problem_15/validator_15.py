# -*- coding: utf-8 -*-
import re


#Tilde checker
def command15(filepath):

    punctuation = "[:',!—_\".?\-;\]\[]"

    match_no_white_space = re.compile(r'(\b\w+~\w*\b)', re.UNICODE)
    match_double_white_space = re.compile(r'\w* ~ \w*', re.UNICODE)
    match_double_tilde = re.compile(r'\w*\s*~~\s*\w*', re.UNICODE)
    match_punctuation_before = re.compile(r"(?<=\w|\W){0}~{0}?".format(punctuation), re.UNICODE)
    match_punctuation_after = re.compile(r"(?<=\s)~{0}".format(punctuation), re.UNICODE)
    match_filler = re.compile(r"#\w*~", re.UNICODE)


    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1

            no_white_space = re.findall(match_no_white_space, line)
            for match in no_white_space:
                found[ln] = [15, 'Incorrect white space', match]

            double_white_space = re.findall(match_double_white_space, line)
            for match in double_white_space:
                found[ln] = [15, 'Incorrect white space', match]

            double_tilde = re.findall(match_double_tilde, line)
            for match in double_tilde:
                found[ln] = [15, 'Double tilde', match]

            touching_punctuation_before = re.finditer(match_punctuation_before, line)
            for match in touching_punctuation_before:
                found[ln] = [15, 'Punctuation touch tilde', match.group()]

            touching_punctuation_after = re.finditer(match_punctuation_after, line)
            for match in touching_punctuation_after:
                found[ln] = [15, 'Punctuation touch tilde', match.group()]

            fillers = re.finditer(match_filler, line)
            for match in fillers:
                found[ln] = [15, 'Filler word with tilde', match.group()]

    return found


if __name__ == '__main__':
    found = command15('../files/TXSportsNation_009.trs')
    for row, hit in found.items():
        print row, ' => ', hit

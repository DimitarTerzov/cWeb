# -*- coding: utf-8 -*-
import re


#Tilde checker
def command15(filepath):

    punctuation = "[:',!—_\".?\-;\]\[]"

    match_no_white_space = re.compile(r'(\b\w+~\w*\b)', re.UNICODE)
    match_no_white_space_end = re.compile(r'\b\w+~\.', re.UNICODE)
    match_double_white_space = re.compile(r'\w* ~ \w*', re.UNICODE)
    match_double_tilde = re.compile(r'\w*\s*~~\s*\w*', re.UNICODE)
    match_capital_letter = re.compile(r'(?P<content>~(?P<word>\b\w+\b))', re.UNICODE)
    match_touching_punctuation = re.compile(r"{0}?~{0}?".format(punctuation), re.UNICODE)
    match_filler = re.compile(r"#\w*~", re.UNICODE)


    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1

            no_white_space = re.findall(match_no_white_space, line)
            for match in no_white_space:
                found[ln] = [15, 'Incorrect white space', match]

            no_white_space_end = re.findall(match_no_white_space_end, line)
            for match in no_white_space_end:
                found[ln] = [15, 'Incorrect white space', match]

            double_white_space = re.findall(match_double_white_space, line)
            for match in double_white_space:
                found[ln] = [15, 'Incorrect white space', match]

            double_tilde = re.findall(match_double_tilde, line)
            for match in double_tilde:
                found[ln] = [15, 'Double tilde', match]

            capital_letter = re.finditer(match_capital_letter, line)
            for match in capital_letter:
                if match.group('word')[0].isupper() and match.group('word')[1].islower():
                    found[ln] = [15, 'Tilde followed by capital and non-capital letter', match.group('content')]

            touching_punctuation = re.finditer(match_touching_punctuation, line)
            for match in touching_punctuation:
                if len(match.group()) > 1 and not ln in found:
                    found[ln] = [15, 'Punctuation touch tilde', match.group()]

            fillers = re.finditer(match_filler, line)
            for match in fillers:
                found[ln] = [15, 'Filler word with tilde', match.group()]

    return found


if __name__ == '__main__':
    found = command15('../files/SEC_Football_004.trs')
    for row, hit in found.items():
        print row, ' => ', hit

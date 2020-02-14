import re


#Tilde checker
def command15(filepath):

    match_no_white_space = re.compile(r'(\b\w+~\w*\b)')
    match_no_white_space_end = re.compile(r'\b\w+~\.')
    match_double_white_space = re.compile(r'\w* ~ \w*')
    match_double_tilde = re.compile(r'\w*\s*~~\s*\w*')

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

    return found


if __name__ == '__main__':
    found = command15('test.trs')
    for row, hit in found.items():
        print row, ' => ', hit

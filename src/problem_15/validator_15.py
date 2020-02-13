import re


#Tilde checker
def command15(filepath):

    #regex = re.compile('([^\s]*)\~(\s?)([^\s]*)')
    match_no_white_space = re.compile(r'(\b\w+~\w*\b)')
    #match_
    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1

            no_white_space = re.findall(match_no_white_space, line)
            for match in no_white_space:
                found[ln] = [15, 'Incorrect white space', match]

            #line = ' ' + line.rstrip("\r\n")

            #for m in re.findall(regex, line):
                #if m[0]:
                    #c1 = m[0][-1:]
                    #if m[0][0] == '#':
                        #found[ln] = [15, 'tag before tilde ~', m[0] + '~' + m[1] + m[2] ]

                    #elif not re.match('[a-zA-Z]', c1):
                        #found[ln] = [15, 'no letter before tilde ~', m[0] + '~' + m[1] + m[2] ]

                    #if m[2]:
                        #if not m[2].lower().startswith(m[0].lower()):
                            #found[ln] = [15, 'incorrect used tilde ~', m[0] + '~' + m[1] + m[2] ]

                        #elif m[0].lower() == m[2].lower():
                            #found[ln] = [15, 'duplicate word', m[0] + '~' + m[1] + m[2] ]

                #if m[1] and not re.match('\s', m[1]):
                    #found[ln] = [15, 'no space after tilde ~', m[0] + '~' + m[1] + m[2] ]
    return found


if __name__ == '__main__':
    found = command15('test.trs')
    for row, hit in found.items():
        print(row, ' => ', hit)

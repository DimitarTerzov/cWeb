#Sound tag validator
def command3(filepath):
    skip_words = ['[no-speech]', '[no—speech]', '[noise]', '[overlap]', '[music]', '[applause]', '[lipsmack]', '[breath]', '[cough]', '[laugh]', '[click]', '[ring]', '[dtmf]', '[sta]', '[cry]', '[prompt]']

    regex = re.compile("\[.*?\]")

    found = {}
    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")
            prev_tag = 'none'

            if '<Speaker' not in line:

                for w in line.split():
                    #if we have something glued to tag

                    if re.match(".*[^ \s、 。 ‧ ？ ！ ，]\[.*?\]", w):
                        found[ln] = [3, 'Missing white space left of sound tag', w]
                    elif re.match("\[.*?\][^ \s.,，。\-?! ].*", w):
                        found[ln] = [3, 'Missing white space right of sound tag', w]
                    else:
                        for m in re.findall(regex, line):
                            if not m in skip_words:
                                found[ln] = [3, 'Sound tag syntax', m + '/' + line]

                            #detect duplicate tags like - [cough][cough]
                            #if we have two of the same tags in a row
                            #and there are one after the other in the line
                            elif prev_tag == m and re.search(re.escape(m)    +"\s*"+WWwhitespace+"*"  +WWpunctuatio+"*"+   re.escape(m), line):
                                found[ln] = [3, 'Sound tag duplicate', m + '/' + line]
                            prev_tag = m
    return found
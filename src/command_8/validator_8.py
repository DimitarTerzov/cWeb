#White space validator
def command8(filepath):
    rv = {}
    patterns = ['\[[^\]*]\]', '&lt;[^;&]*&gt;', '#[^ #\.,，。\s?!~‘s-]*', '\(\(\)\)', '\(\([^\)]*\)\)']

    for pat in patterns:
        found = command8_real(f, pat)
        rv.update(found)
    return rv


def command8_real(filepath, pattern):

    reg_allowed = '[\.,，。\s?!~‘s-]'
    regex_pat = '(.)' + pattern + '(.)'

    regex = re.compile('.' + pattern + '.')

    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            #if line starts with < and ends in >
            if line.startswith('<') and line.endswith('>'):
                #we skip everythin between <>
                continue

            #put spaces in front/end of line, to avoid checking for startswith/endswith for each token
            line = ' ' + line + ' '

            for m in re.findall(regex, line):
                matchObj = re.match(regex_pat, m)
                if not matchObj:
                    found[ln] =  [8, 'Missing white space (syntax)', m]
                else:
                    lC = matchObj.group(1)
                    rC = matchObj.group(2)

                    #if language is not in the list
                    if not re.match('[\s　。，]', lC):
                        found[ln] =  [8, 'Missing white space (invalid left char)', lC + '/' + m]
                    elif not re.match(reg_allowed, rC):
                        found[ln] =  [8, 'Missing white space (invalid right char)', rC + '/' + m]
    return found

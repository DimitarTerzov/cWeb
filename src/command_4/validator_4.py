import re


#Initial tag validator
def command4(filepath):

    regex = re.compile("&lt;[intal]+&gt;[^;&]*&lt;[/intal]+&gt;")

    found = {}
    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            for m in re.findall(regex, line):
                if not re.match('&lt;initial&gt; .* &lt;/initial&gt;', m):
                    found[ln] = [4, 'Initial tag error', m]
    return found

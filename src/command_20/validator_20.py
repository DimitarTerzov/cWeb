def command20(filepath):
    # WWpunctuatio found in this file at: line 13
    regex = re.compile("&lt;initial&gt;[a-zA-z\s]*" + WWpunctuatio + "+[a-zA-z\s]*&lt;\/initial&gt;|&lt;lang:\s?[a-zA-Z]*&gt;.*" + WWpunctuatio + "+\s+&lt;\/lang:\s?[a-zA-z]*&gt;")

    found = {}

    with open (filepath, 'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            for m in re.findall(regex, line):

                if re.match("&lt;initial&gt;", m):


                    if not re.search("&lt;initial&gt;\s?[A-Za-zÀ-ÖØ-öø-ÿ]{1}\.\s?&lt;\/initial&gt;", line):
                        found[ln] = [20, 'Disallowed punctuation inside initial tag', m]
                    else:
                        if re.search("&lt;initial&gt;\s?[A-Za-zÀ-ÖØ-öø-ÿ]{1}\.\s?&lt;\/initial&gt;\s*$", line) != None:
                            found[ln] = [20, 'Disallowed punctuation inside initial tag', m]

    return found

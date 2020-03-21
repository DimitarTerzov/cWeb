def command23(filepath):
    bad_strings = ['Who nb=', 'Topic id=', 'Event' 'mode=', 'channel=', 'fidelity=']
    found = {}
    regex = re.compile(".*<(.*)>.*")

    with open (filepath, 'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            inner = re.findall(regex, line)
            # < inner >
            for txt in inner:
                for bad in bad_strings:

                    if bad in txt:
                        if bad == 'Who nb=':
                            found[ln] = [23, 'Do not create turns with multiple speakers.', '(' + bad + ') | ' + line]
                            break   #print only one bad string per line
                        elif bad == 'Topic id=':
                            found[ln] = [23, 'Do not create topics', '(' + bad + ') | ' + line]
                            break
                        elif bad == 'Event':
                            found[ln] = [23, 'Do not create events', '(' + bad + ') | ' + line]
                            break
                        elif bad == 'mode=':
                            found[ln] = [23, 'Do not change the mode setting', '(' + bad + ') | ' + line]
                            break
                        elif bad == 'channel=':
                            found[ln] = [23, 'Do not change the channel setting', '(' + bad + ') | ' + line]
                            break
                        elif bad == 'fidelity=':
                            found[ln] = [23, 'Do not change the fidelity setting', '(' + bad + ') | ' + line]
                            break
    return found
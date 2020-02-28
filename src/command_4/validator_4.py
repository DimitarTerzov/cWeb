import re


#Initial tag validator
def command4(filepath):

    punctuation = "[^'.,!?\s:;-_\"]"
    allowed_characters = "s"
    regex = re.compile(r"(?P<content>(?P<before_first>(\b\w*\b)|[\S\w]+)?(?P<first_open>&lt;|\<)(?P<first_tag>[int\w\s/\\]+)(?P<first_close>&gt;|\>)(?P<inner_text>.*?)(?P<second_open>&lt;|\<)(?P<forward>[\\/\s]*)(?P<second_tag>[int\w\s]+)(?P<second_close>&gt;|\>)(?P<after_second>\b\w*\b|{}+)?)".format(punctuation), re.UNICODE)

    found = {}
    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n").decode('utf')

            for m in re.finditer(regex, line):

                # Check tag syntax
                if (
                    m.group('first_open') != '&lt;' or
                    m.group('first_close') != '&gt;' or
                    m.group('second_open') != '&lt;' or
                    m.group('second_close') != '&gt;' or
                    m.group('forward') != '/'
                ):
                    found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]
                    continue

                # Check tag spelling
                if (
                    m.group('first_tag') != 'initial' or
                    m.group('second_tag') != 'initial'
                ):
                    found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]
                    continue

                if (
                    m.group('after_second') is not None and
                    not m.group('after_second') in allowed_characters
                ):
                    found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]
                    continue

                # Check for incorrect white space
                if (
                    m.group('before_first') is not None or
                    not m.group('inner_text').startswith(' ') or
                    not m.group('inner_text').endswith(' ')
                ):
                    found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]
                    continue

                # Check for errors in text
                inner_text = m.group('inner_text')
                inner_content = inner_text.split()
                # If no text in tag -> error
                if not inner_content:
                    found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]

                elif len(inner_content) == 1:
                    content = inner_content[0]
                    # Catch anything different from pattern `W`
                    if len(content) == 1 and re.match(r'\W', content, re.UNICODE):
                        found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]

                    # Catch anything different from pattern `WE` and `W.`
                    elif len(content) == 2 and not re.match(r'^\w+\.?$', content, re.UNICODE):
                        found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]

                    # Catch anything different from pattern `WEB`
                    elif len(content) > 2 and re.match(r'\w*\W', content, re.UNICODE):
                        found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]

                # If text doesn't feet pattern `W. E. B.` -> error
                elif len(inner_content) > 1:
                    for content in inner_content:
                        if not re.match(r'^\w\.$', content, re.UNICODE):
                            found[ln] = [4, 'Initial tag error', m.group('content').encode('ascii', 'replace')]

    return found


if __name__ == '__main__':
    found = command4('../files/test_4.trs')
    keys = found.keys()
    keys = sorted(keys)
    print
    print len(keys)
    for key in keys:
        print key, found[key]

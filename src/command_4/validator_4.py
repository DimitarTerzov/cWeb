import re


#Initial tag validator
def command4(filepath):

    regex = re.compile(r"(?P<content>(?P<before_first>\b\w*\b)?(?P<first_open>&lt;|\<)(?P<first_tag>[int\w]+)(?P<first_close>&gt;|\>)(?P<inner_text>.*?)(?P<second_open>&lt;|\<)(?P<forward>[\/]*)(?P<second_tag>[int\w]+)(?P<second_close>&gt;|\>)(?P<after_second>\b\w*\b)?)", re.UNICODE)
    punctuation_marks = u""":,-'—_!".?;"""

    found = {}
    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n").decode('utf')

            for m in re.finditer(regex, line):
                print ln, m.group('content'), '|', m.group('inner_text')

                # Check tag syntax
                if (
                    m.group('first_open') != '&lt;' or
                    m.group('first_close') != '&gt;' or
                    m.group('second_open') != '&lt;' or
                    m.group('second_close') != '&gt;' or
                    m.group('forward') != '/'
                ):
                    found[ln] = [4, 'Initial tag error', m.group('content')]
                    continue

                # Check tag spelling
                if (
                    m.group('first_tag') != 'initial' or
                    m.group('second_tag') != 'initial'
                ):
                    found[ln] = [4, 'Initial tag error', m.group('content')]
                    continue

                # Check for incorrect white space
                if (
                    m.group('before_first') is not None or
                    m.group('after_second') is not None or
                    not m.group('inner_text').startswith(' ') or
                    not m.group('inner_text').endswith(' ')
                ):
                    found[ln] = [4, 'Initial tag error', m.group('content')]
                    continue

                # Check for errors in text
                inner_text = m.group('inner_text')
                inner_content = inner_text.split()
                if not inner_content:
                    found[ln] = [4, 'Initial tag error', m.group('content')]

                elif len(inner_content) > 1:
                    for content in inner_content:
                        if len(content) != 2 and not content.endswith('.'):
                            found[ln] = [4, 'Initial tag error', m.group('content')]

                elif len(inner_content) == 1:
                    content = inner_content[0]
                    if content[-1] in punctuation_marks:
                        found[ln] = [4, 'Initial tag error', m.group('content')]

    return found


if __name__ == '__main__':
    found = command4('../files/initial tag but inside spacing.trs')
    keys = found.keys()
    keys = sorted(keys)
    print
    print len(keys)
    for key in keys:
        print key, found[key]

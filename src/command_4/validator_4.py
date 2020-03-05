# -*- coding: utf-8 -*-
import re


#Initial tag validator
def command4(filepath):
    import io

    punctuation = "[^'.,!?\s:;-_—\"]"
    allowed_characters_after_tag = "s"
    allowed_expressions_before_tag = ["l'"]
    regex = re.compile(r"(?P<content>(?P<before_first>(\b\w*\b)|[\S\w]+)?(?P<first_open>&lt;|\<)(?P<first_tag>[int\w\s/\\]+)(?P<first_close>&gt;|\>)(?P<inner_text>.*?)(?P<second_open>&lt;|\<)(?P<forward>[\\/\s]*)(?P<second_tag>[int\w\s]+)(?P<second_close>&gt;|\>)(?P<after_second>\b\w*\b|{}+)?)".format(punctuation), re.UNICODE)

    found = {}
    with io.open(filepath, 'r', encoding='utf') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")

            for m in re.finditer(regex, line):
                error_tag = m.group('content').encode('utf')

                # Check tag syntax
                if (
                    m.group('first_open') != '&lt;' or
                    m.group('first_close') != '&gt;' or
                    m.group('second_open') != '&lt;' or
                    m.group('second_close') != '&gt;' or
                    m.group('forward') != '/'
                ):
                    found[ln] = [4, 'Initial tag error', error_tag]
                    continue

                # Check tag spelling
                if (
                    m.group('first_tag') != 'initial' or
                    m.group('second_tag') != 'initial'
                ):
                    found[ln] = [4, 'Initial tag error', error_tag]
                    continue

                # Check for disallowed expressions before tag
                if (
                    m.group('before_first') is not None and
                    not m.group('before_first') in allowed_expressions_before_tag
                ):
                    found[ln] = [4, 'Initial tag error', error_tag]
                    continue

                # Check for disallowed expressions after tag
                if (
                    m.group('after_second') is not None and
                    not m.group('after_second') in allowed_characters_after_tag
                ):
                    found[ln] = [4, 'Initial tag error', error_tag]
                    continue

                # Check for incorrect white space
                if (
                    not m.group('inner_text').startswith(' ') or
                    not m.group('inner_text').endswith(' ')
                ):
                    found[ln] = [4, 'Initial tag error', error_tag]
                    continue

                # Check for errors in text
                inner_text = m.group('inner_text')
                inner_content = inner_text.split()
                # If no text in tag -> error
                if not inner_content:
                    found[ln] = [4, 'Initial tag error', error_tag]

                elif len(inner_content) == 1:
                    content = inner_content[0]
                    # Catch anything different from pattern `W`
                    if len(content) == 1 and re.match(r'\W', content, re.UNICODE):
                        found[ln] = [4, 'Initial tag error', error_tag]

                    # Catch anything different from pattern `WE` and `W.`
                    elif len(content) == 2 and not re.match(r'^\w+\.?$', content, re.UNICODE):
                        found[ln] = [4, 'Initial tag error', error_tag]

                    # Catch anything different from pattern `WEB`, `Ph.D.`
                    elif len(content) > 2:
                        if re.match(r'[\w.]*', content, re.UNICODE).group() != content:
                            found[ln] = [4, 'Initial tag error', error_tag]

                # If text doesn't feet pattern `W. E. B.` -> error
                elif len(inner_content) > 1:
                    for content in inner_content:
                        if not re.match(r'^\w\.$', content, re.UNICODE):
                            found[ln] = [4, 'Initial tag error', error_tag]

    return found


if __name__ == '__main__':
    found = command4('../files/initial tag but inside spacing.trs')
    keys = found.keys()
    keys = sorted(keys)
    print len(keys)
    for key in keys:
        print key, found[key], found[key][2]

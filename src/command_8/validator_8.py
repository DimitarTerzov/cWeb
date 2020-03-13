#White space validator
def command8(filepath):
    rv = {}
    patterns = ['\[[^\]*]\]', '&lt;[^;&]*&gt;', '#[^ #\.,，。\s?!~‘s-]*', '\(\(\)\)', '\(\([^\)]*\)\)']

    for pat in patterns:
        found = command8_real(f, pat)
        rv.update(found)
    return rv

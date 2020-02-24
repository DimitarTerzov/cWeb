import string


#Filler word validator
def command7(filepath):

    #default english skip tags
    skip_tags = ['#uh', '#um', '#ah', '#er', '#hm']

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

            #if we find a skip tag, remove it from line
            changed = True
            while changed:
                for w in skip_tags:
                    pos = line.find(w)
                    if pos >= 0:
                        line = line.replace(w, '')
                        changed = True
                    else:
                        changed = False

            for word in line.split():
                if word.startswith('<') and word.endswith('>'):
                    continue

                # if the word contains a #, after all skip tags where removed
                # if word.find('#') >= 0:
                if word[0]=='#':
                    word = '#' + word.translate(str.maketrans('', '', string.punctuation))
                    if word.lower() in [x.lower() for x in skip_tags]:
                        found[ln] = [7, 'Invalid filler tag',  word + '/' + line]

    return found

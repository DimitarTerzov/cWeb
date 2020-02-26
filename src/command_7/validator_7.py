import string


#Filler word validator
def command7(filepath):

    #default english skip tags
    skip_tags = ['#uh', '#um', '#ah', '#eh', '#hm']

    found = {}

    with open(filepath,'r') as f:
        ln = -1
        for line in f:
            ln = ln + 1
            line = line.rstrip("\r\n")


    return found


if __name__ == '__main__':
    found = command7()

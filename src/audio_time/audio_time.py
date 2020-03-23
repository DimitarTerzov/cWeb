import re

def build_sync_times(filepath):
    sync_t = {}

    last_sync = ""

    with open(filepath) as f:
        ln = -1
        for line in f:
            ln = ln + 1

            line = line.rstrip("\r\n")
            if re.match("<Sync time=\"[\s\d\.]+\"/>", line):
                last_sync = line
            sync_t[ln] = last_sync
    return sync_t

import pytest


def temporary_file(tmpdir, content):
    file_ = str(tmpdir.mkdir("sub").join("tilde.trs"))
    with open(file_, 'a') as f:
        for line in content:
            f.write(line)
    return file_

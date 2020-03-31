# -*- coding: utf-8 -*-
from __future__ import print_function
import os

import pytest

from command_0.validator_0 import command0
from utils import temporary_file, LANGUAGE_CODES


CONTENT = [
    [u'<Trans scribe="ell-001" audio_filename="EPT_Political_news_118" version="9" version_date="200227">\n'],      # 0
    [u'<Trans scribe="bul-011" audio_filename="EPT_Political_news_118" version="9" version_date="200227">\n'],     # 1
    [u'<Trans scribe="ellis-101" audio_filename="EPT_Political_news_118" version="9" version_date="200227">\n'],    # 2
    [u'<Trans scribe="ell-a01" audio_filename="EPT_Political_news_118" version="9" version_date="200227">\n'],       # 3
    [u'<Trans scribe="ell-0010" audio_filename="EPT_Political_news_118" version="9" version_date="200227">\n'],     # 4
]


def test_command_0(tmpdir):
    for row in range(5):
        file_ = temporary_file(tmpdir, CONTENT[row])
        found = command0(file_)

        for key, value in found.items():
            print(key, value)

        if row in [2, 3, 4]:
            assert 0 in found
        else:
            assert 'transcriber_id' in found

    assert 0

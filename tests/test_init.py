"""
Test module for . . .
"""
# Standard library imports
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import logging
from os.path import abspath, dirname, join, realpath, relpath
from sys import path

# Third party imports
import pytest

# Local imports

logger = logging.getLogger(__name__)

test_dir = realpath(dirname(__file__))
src_dir = abspath(join(test_dir, '..'))
path.append(src_dir)
print(path)

import pypiserver


@pytest.mark.parametrize('conf_options', [
    {},
    {'root': '~/stable_packages'},
    {'root': '~/unstable_packages', 'authenticated': 'upload',
     'passwords': '~/htpasswd'}
])
def test_paste_app_factory(conf_options, monkeypatch):
    """Test the paste_app_factory method"""
    monkeypatch.setattr('pypiserver.core.configure',
                        lambda **x: (x, [x.keys()]))
    pypiserver.paste_app_factory({}, **conf_options)




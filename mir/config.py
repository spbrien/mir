#!/usr/bin/env python

from __future__ import absolute_import
import os
import json
from six.moves import range


def find_root():
    working_dir = os.getcwd().split(os.sep)
    length = len(working_dir) + 1
    build_paths = [x for x in ['/'.join(working_dir[:x]) for x in range(length)] if x != '']
    paths = [x for x in reversed(build_paths)]
    for path in paths:
        test_root = os.path.join(path, '.mir')
        if os.path.isfile(test_root):
            return path
    return None


def get_config(root_dir):
    if root_dir:
        c = os.path.join(root_dir, '.mir')
        with open(c, 'r') as f:
            config = json.load(f)
        return config
    return None


ROOT_DIR = find_root()
HAS_PROJECT_ROOT = True if ROOT_DIR else False
APP_DIR = os.path.join(ROOT_DIR, 'application') if HAS_PROJECT_ROOT else os.getcwd()
# CONFIG = get_config(ROOT_DIR)

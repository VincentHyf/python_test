#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Description:显示有关运行此脚本的操作系统的一些信息

import platform as pl


profile = [
    'architecture',
    'linux_distribution',
    'mac_ver',
    'machine',
    'node',
    'platform',
    'processor',
    'python_build',
    'python_compiler',
    'python_version',
    'release',
    'system',
    'uname',
    'version'
]


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

for key in profile:
    if hasattr(pl, key):
        print(key + ": " + str(getattr(pl, key)()))
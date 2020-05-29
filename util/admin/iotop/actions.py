#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Süleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import shelltools

def build():
    shelltools.system("sed -i '7,13d' setup.py")
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")

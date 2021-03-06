#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get
import os

shelltools.export("CC","clang")
shelltools.export("CXX","clang++")
del os.environ['LD']

def setup():
    shelltools.system("./configure --prefix=/usr --with-system-libs")

def build():
    shelltools.system("make")

def install():
    autotools.install()

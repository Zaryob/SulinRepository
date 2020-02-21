#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get
import os

WORKDIR="yaru-20.04.1"

def setup():
    shelltools.system("mkdir build")

def build():
    _env=os.environ.copy()
    os.environ.clear()
    shelltools.system("meson build")
    os.environ.update(_env)

def install():
    shelltools.system("cd build ; DESTDIR='{}' ninja install".format(get.installDIR()))

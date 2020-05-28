#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import shelltools
from inary.actionsapi import mesontools
from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import get
import os 
def setup():
    if not os.path.exists("budgie-desktop"):
        shelltools.system("git clone https://github.com/solus-project/budgie-desktop")
    shelltools.cd("budgie-desktop")
    shelltools.system("git checkout 7a402a86bfb7317ea648a13e0effd19cfce3fa91")
    shelltools.system("git submodule init")
    shelltools.system("git submodule update")
    mesontools.meson_configure("-Dselinux=false  \
    -D packagekit=false")

def build():
    shelltools.cd("budgie-desktop")
    mesontools.ninja_build()

def install():
    shelltools.cd("budgie-desktop")
    mesontools.ninja_install()

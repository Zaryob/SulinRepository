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
        shelltools.system("git clone  --depth=1 https://github.com/solus-project/budgie-desktop")
    shelltools.cd("budgie-desktop")
    shelltools.system("git submodule init")
    shelltools.system("git submodule update")
    mesontools.meson_configure("-Dselinux=false  \
    -D packagekit=false -D with-desktop-icons=none -D with-polkit=false")

def build():
    shelltools.cd("budgie-desktop")
    mesontools.ninja_build()

def install():
    shelltools.cd("budgie-desktop")
    mesontools.ninja_install()

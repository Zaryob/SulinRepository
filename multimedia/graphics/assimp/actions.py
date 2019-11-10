#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import cmaketools
from inary.actionsapi import get
from inary.actionsapi import inarytools


def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_BUILD_TYPE=Release \
        -DASSIMP_BUILD_SAMPLES=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())


    inarytools.dodoc("LICENSE", "Readme.md", "README")

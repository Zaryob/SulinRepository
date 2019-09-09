#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import cmaketools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    options = "\-DCMAKE_BUILD_TYPE=Release \
                -DFREEGLUT_BUILD_DEMOS=OFF \
              "

    if get.buildTYPE() == "emul32":

        shelltools.export("CFLAGS", "-m32")
        shelltools.export("CXXFLAGS", "-m32")

        options += "-DFREEGLUT_BUILD_DEMOS=OFF \
                   "

    cmaketools.configure(options)

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    inarytools.dodoc("AUTHORS", "ChangeLog", "README")
    inarytools.dohtml("doc/*")

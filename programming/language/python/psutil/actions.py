#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    if get.buildTYPE()=="rebuild_python":
        ver="2"
    else:
        ver="3"
    pythonmodules.compile(pyVer=ver)

def install():
    if get.buildTYPE()=="rebuild_python":
        ver="2"
    else:
        ver="3"
    pythonmodules.install(pyVer=ver)
    #inarytools.domove("/usr/local/", "/usr/lib")

    inarytools.dodoc("LICENSE", "README.rst", "INSTALL.rst")

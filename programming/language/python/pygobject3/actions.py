#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import pythonmodules
from inary.actionsapi import shelltools
from inary.actionsapi import get

def build():

    if get.buildTYPE()=="rebuild_python":
        shelltools.export("PYTHON", "/usr/bin/python3.7")
        pythonmodules.compile(pyVer="3")
    else:
        shelltools.export("PYTHON", "/usr/bin/python2.7")
        pythonmodules.compile(pyVer="2")

def install():
    if get.buildTYPE()=="rebuild_python":
        pythonmodules.install(pyVer="3")
    else:
        pythonmodules.install(pyVer="2")


#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import get

WorkDir="idna-2.10"

def setup():
    pythonmodules.compile()
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install()
    pythonmodules.install(pyVer="3")


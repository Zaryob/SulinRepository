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

WorkDir="urllib3-1.25.10"

def setup():
    pythonmodules.compile(pyVer="3")
    pythonmodules.compile()

def install():
    pythonmodules.install(pyVer="3")
    pythonmodules.install()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import shelltools
from inary.actionsapi import get
from inary.actionsapi import inarytools

WorkDir="wheel-%s" % get.srcVERSION()

def setup():
    pythonmodules.compile(pyVer = "3")
    pythonmodules.compile()


def install():
    pythonmodules.install()
    inarytools.rename("/usr/bin/wheel", "wheel-2.7")
    pythonmodules.install(pyVer = "3")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "Cython-%s" % get.srcVERSION()

def build():
    pythonmodules.compile(pyVer="2")

def install():
    pythonmodules.install(pyVer="2")
    inarytools.dodoc("COPYING*", "README*", "PKG-INFO")


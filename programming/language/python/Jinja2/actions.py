#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools

def build():
    pythonmodules.compile(pyVer = "3")
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pythonmodules.install(pyVer = "3")
    inarytools.dodoc("LICENSE*", "MANIFEST*", "PKG-INFO", "README*")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    #remove broken application launcher
    inarytools.removeDir("/usr/share/applications")
    inarytools.dodoc("COPYING", "PKG-INFO", "NEWS*", "README*")

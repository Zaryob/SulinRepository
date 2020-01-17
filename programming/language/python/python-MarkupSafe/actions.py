#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import get
from inary.actionsapi import shelltools

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

WorkDir = "MarkupSafe-%s" % get.srcVERSION()

def build():
    pythonmodules.compile(pyVer="2")
    pythonmodules.compile(pyVer="3")

def check():
    pythonmodules.compile("test", pyVer="2")
    pythonmodules.compile("test", pyVer="3")

def install():
    pythonmodules.install(pyVer="2")
    pythonmodules.install(pyVer="3")

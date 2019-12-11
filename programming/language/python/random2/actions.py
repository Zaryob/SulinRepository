#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools

def build():
    pythonmodules.compile(pyVer="3")
    pythonmodules.compile(pyVer="2")

def install():
    pythonmodules.install(pyVer="3")
    pythonmodules.install(pyVer="2")

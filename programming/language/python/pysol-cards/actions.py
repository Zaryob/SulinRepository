#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def install():
    pythonmodules.install("--optimize=1")
    pythonmodules.install("--optimize=1", pyVer="3")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import get
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")


def install():
    pythonmodules.install(pyVer="3")
    pythonmodules.install()

    pythonmodules.fixCompiledPy()


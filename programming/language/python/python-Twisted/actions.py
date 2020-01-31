#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

WorkDir = "twisted-twisted-%s" % (get.srcVERSION())

def install():
    pythonmodules.install()


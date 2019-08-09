#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools

def build():
    pythonmodules.compile(pyVer="2")

def install():
    pythonmodules.install("--no-version-script \
                           --standalone-lib \
                           --install-scripts=/usr/bin \
                           --install-data=/usr/share",pyVer="2")

    inarytools.dodoc("CHANGES*", "LICENSE*", "README*", "RELEASE*")

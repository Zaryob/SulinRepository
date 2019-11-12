#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import mesontools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import cmaketools

def setup():
    inarytools.dosed("CMakeLists.txt", 'NOT BUILD_SHARED_LIBS', 'TRUE')
    shelltools.makedirs("inaryPackageBuild")
    shelltools.cd("inaryPackageBuild")
    cmaketools.configure("-G Ninja", sourceDir="..")

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()

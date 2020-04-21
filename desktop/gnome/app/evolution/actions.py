#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import mesontools
from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    cmaketools.configure("-DENABLE_PST_IMPORT=OFF     \
      -DENABLE_YTNEF=OFF          \
      -DENABLE_TEXT_HIGHLIGHT=OFF \
      -DENABLE_CONTACT_MAPS=OFF   -G Ninja .")

def build():
   shelltools.system("ninja")

def install():
    shelltools.system("DESTDIR={} ninja install".format(get.installDIR()))

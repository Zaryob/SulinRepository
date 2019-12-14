#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import cmaketools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get

shelltools.export("CFLAGS", "%s -lpthread" % get.CFLAGS())

def setup():
    cmaketools.configure("-Denable-ladspa=ON \
                          -DLIB_SUFFIX=\"\"")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    inarytools.dodoc("AUTHORS", "ChangeLog", "LICENSE", "README*", "THANKS*")

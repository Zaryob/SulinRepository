#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -fstack-protector-all" % get.CFLAGS())

    mesontools.cmake_configure("-DCMAKE_BUILD_TYPE=Release \
                                -DCMAKE_INSTALL_PREFIX=/usr \
                                -DCMAKE_INSTALL_LIBDIR=lib \
                                -DCMAKE_INSTALL_RPATH= \
                                -DCMAKE_SKIP_RPATH=ON")
def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")

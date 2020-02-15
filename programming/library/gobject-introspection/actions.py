#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


def setup():
    if get.buildTYPE()=="emul32":
        shelltools.export("PKG_CONFIG_LIBDIR","/usr/lib32/pkgconfig")
        shelltools.export("PKG_CONFIG_PATH","/usr/share/pkgconfig")

    mesontools.meson_configure('-D cairo=enabled ')

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()

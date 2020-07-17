#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import mesontools
from inary.actionsapi import get
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools

if get.buildTYPE()=="emul32":
    shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")

def setup():
    mesontools.meson_configure("-Dgtk-doc=false ")

def build():
    mesontools.ninja_build()


def install():
    mesontools.ninja_install()

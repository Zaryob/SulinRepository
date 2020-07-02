#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import get


def setup():
    mesontools.meson_configure("-D graphite=disabled" if get.buildTYPE() == "emul32" else "-D graphite=enabled" )

def build():
    mesontools.ninja_build()
def install():
    mesontools.ninja_install()
    if get.buildTYPE()=="emul32":
        inarytools.domove("/usr/*.so*", "/usr/lib32")
        inarytools.domove("/usr/cmake", "/usr/lib32")
        inarytools.domove("/usr/girepository-1.0", "/usr/lib32")
        inarytools.domove("/usr/pkgconfig", "/usr/lib32")
        return
    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

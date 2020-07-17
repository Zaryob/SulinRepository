# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools


def setup():
    mesontools.meson_configure()

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()
    if get.buildTYPE()=="emul32":
        inarytools.domove("/usr/*.so*", "/usr/lib32/")
        inarytools.domove("/usr/gstreamer-1.0", "/usr/lib32/")
        inarytools.domove("/usr/girepository-1.0", "/usr/lib32/")
        inarytools.domove("/usr/pkgconfig", "/usr/lib32/")

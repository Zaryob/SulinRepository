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
    options=""
    if get.buildTYPE()=="emul32":
        shelltools.export("CC", "gcc -m32 -mstackrealign -mfpmath=sse")
        shelltools.export("CXX", "g++ -m32 -mstackrealign -mfpmath=sse")
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        shelltools.system("patch -p1 < multilib.patch")
        options+="-Dtests=false"
    mesontools.meson_configure(options)


def build():
    if get.buildTYPE()=="emul32":
        shelltools.export("CC", "gcc -m32 -mstackrealign -mfpmath=sse")
        shelltools.export("CXX", "g++ -m32 -mstackrealign -mfpmath=sse")
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

    mesontools.ninja_build()

def install():
    if get.buildTYPE()=="emul32":
        shelltools.system('DESTDIR="{}/emul32" ninja install -C inaryPackageBuild'.format(get.installDIR()))
        inarytools.domove("/emul32/usr/lib32", "/usr/lib32")
        inarytools.domove("/emul32/usr/bin/*", "/usr/bin/32")
        inarytools.removeDir("/emul32")
        return
    else:
        mesontools.ninja_install()

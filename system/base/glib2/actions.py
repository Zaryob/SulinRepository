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
    mesontools.meson_configure()

def build():
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

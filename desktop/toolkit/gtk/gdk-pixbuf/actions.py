#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import mesontools
from inary.actionsapi import get
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools

def setup():
    mesontools.meson_configure("-Denable-gtk-doc=false ")

def build():
    mesontools.ninja_build()


def install():
    if get.buildTYPE()=="emul32":
        shelltools.system('DESTDIR="{}/emul32" ninja install -C inaryPackageBuild'.format(get.installDIR()))
        inarytools.domove("/emul32/usr/bin/gdk-pixbuf-query-loaders", "/usr/bin", "gdk-pixbuf-query-loaders-32")
        inarytools.domove("/emul32/usr/lib32", "/usr/")
        inarytools.removeDir("/emul32")
        return
    else:
        mesontools.ninja_install()
        inarytools.dosym("/usr/bin/gdk-pixbuf-query-loaders", "/usr/bin/gdk-pixbuf-query-loaders-64")

    inarytools.dodoc("CONTRIBUTING.md", "COPYING", "NEWS", "README.md")

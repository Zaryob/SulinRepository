#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.export("OPTIMIZER", get.CFLAGS())
    shelltools.export("DEBUG", "-DNDEBUG")

    autotools.rawConfigure("--libdir=/lib \
                            --disable-static  \
                            --mandir=/usr/share/man \
                            --libexecdir=/lib \
                            --bindir=/bin")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.chmod("%s/lib/libacl.so.*.*.*" % get.installDIR(), 0o755)
    shelltools.copytree("%s/lib/pkgconfig" % get.installDIR(), "%s/usr/lib/pkgconfig" % get.installDIR())
    inarytools.removeDir("/lib/pkgconfig")

    inarytools.dodoc("README")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

if get.buildTYPE() == "emul32":
    shelltools.export("CFLAGS","-m32")
    shelltools.export("CXXFLAGS","-m32")
    shelltools.export("LDFLAGS","-m32")

def build():
    autotools.make()
    autotools.make("zstdmt")
    autotools.make("-C contrib/pzstd")

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("LIBDIR=/usr/lib32 \
         PKGCONFIGDIR=/usr/lib32/pkgconfig \
         PREFIX=/usr \
         DESTDIR=%s" % get.installDIR())
        shelltools.system("sed -i s/lib$/lib32/ {}/usr/lib32/pkgconfig/libzstd.pc || true".format(get.installDIR()))
        return
    else:
        autotools.rawInstall("LIBDIR=/usr/lib PREFIX=/usr DESTDIR=%s" % get.installDIR())
    inarytools.dobin("zstdmt")
    inarytools.dobin("contrib/pzstd/pzstd")
    inarytools.dodoc("LICENSE", "README*")

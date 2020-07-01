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
    shelltools.export("CFLAGS", get.CFLAGS().replace("-fstack-protector",""))
    shelltools.export("CPPFLAGS", get.CXXFLAGS().replace("-fstack-protector",""))
    autotools.configure("--without-mpicc")

def build():
    autotools.make()

def install():
    if get.buildTYPE()=="emul32":
        shelltools.system("make install DESTDIR={}/emul32".format(get.installDIR()))
        shelltools.system("mkdir {0}/usr && mv {0}/emul32/usr/lib32 {0}/usr/".format(get.installDIR()))
        shelltools.system("rm -rf {0}/emul32/".format(get.installDIR()))
        shelltools.system("sed -i 's|emul32|usr|' {0}/usr/lib32/pkgconfig/*.pc".format(get.installDIR()))
        return
    autotools.install()
    inarytools.dodoc("AUTHORS", "FAQ.txt", "NEWS", "README*")

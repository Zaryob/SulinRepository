#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import cmaketools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    if get.buildTYPE() == "emul32":
        inarytools.insinto("/usr/lib32", "bin/libopenjp2*")
        inarytools.insinto("/usr/lib32/pkgconfig", "libopenjp2.pc")
        inarytools.dosed("%s/usr/lib32/pkgconfig/libopenjp2.pc" % get.installDIR(),
                        get.emul32prefixDIR(),
                        get.defaultprefixDIR())
        inarytools.dosed("%s/usr/lib32/pkgconfig/libopenjp2.pc" % get.installDIR(),
                        "/lib",
                        "/lib32")
        return

    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dosym("openjpeg-2.3/openjpeg.h", "/usr/include/openjpeg.h")

    inarytools.dodoc("README*")

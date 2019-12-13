#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def build():
    inarytools.dosed("src/Makefile", "=-shared", r"= -Wl,-O1,--as-needed -shared")
    if get.buildTYPE() == "emul32":
        inarytools.dosed(".", "\/lib$", r"/lib%s\n" % "32" if get.buildTYPE() == "emul32" else "", filePattern="Makefile")
    autotools.make()


def install():

    if get.buildTYPE() == "emul32":
        autotools.rawInstall("prefix=%s/usr \
                              includedir=%s/usr/include \
                              libdir%s/=usr/lib32 " % ((get.installDIR(), ) * 3))
        inarytools.remove("/usr/lib32/libaio.a")
    else:
        autotools.rawInstall("prefix=%s/usr \
                              includedir=%s/usr/include \
                              libdir%s/=usr/lib " % ((get.installDIR(), ) * 3))
        inarytools.remove("/usr/lib/libaio.a")

        inarytools.dodoc("ChangeLog", "COPYING", "TODO")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt.

from inary.actionsapi import cmaketools
from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get


def setup():
    shelltools.copy("INSTALL/make.inc.gfortran", "make.inc")

    if get.ARCH() == "x86_64":
        inarytools.dosed("make.inc", "-O2", "%s -fPIC -m64 -funroll-all-loops" % get.CFLAGS())
        inarytools.dosed("make.inc", "NOOPT    =", "NOOPT    =-m64 -fPIC ")
    else:
        inarytools.dosed("make.inc", "-O2", "%s -fPIC -funroll-all-loops" % get.CFLAGS())

    shelltools.makedirs("build")
    shelltools.cd("build")
    options = "-DCMAKE_INSTALL_LIBDIR=lib \
               -DBUILD_SHARED_LIBS=ON \
               -DBUILD_TESTING=OFF"

    if get.buildTYPE() == "static":
        options = "-DCMAKE_INSTALL_LIBDIR=lib \
                   -DBUILD_SHARED_LIBS=OFF \
                   -DBUILD_TESTING=OFF"

    cmaketools.configure(options, sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../")

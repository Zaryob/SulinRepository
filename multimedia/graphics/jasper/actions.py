#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import libtools
from inary.actionsapi import get

def setup():
    shelltools.makedirs("inary-build")
    shelltools.cd("inary-build")
    cmaketools.configure("    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib{} \
    -DCMAKE_BUILD_TYPE=Release \
    -DJAS_ENABLE_OPENGL=ON \
    -DJAS_ENABLE_LIBJPEG=ON \
    -DJAS_ENABLE_AUTOMATIC_DEPENDENCIES=OFF \
    -DCMAKE_SKIP_RPATH=ON".format("32" if get.buildTYPE() == "emul32" else ""), sourceDir="..")

def build():
    shelltools.cd("inary-build")

    cmaketools.make()

def install():
    shelltools.cd("inary-build")

    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

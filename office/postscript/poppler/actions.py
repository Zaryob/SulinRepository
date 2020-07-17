#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import cmaketools
from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools


def setup():

    shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig" if get.buildTYPE() == "emul32" else  "/usr/lib/pkgconfig" )
    if get.buildTYPE() == "emul32":
        shelltools.system("sed -i 's|ENABLE_NSS3 ON|ENABLE_NSS3 OFF|' CMakeLists.txt")

    options = "-DCMAKE_BUILD_TYPE=Release   \
               -DCMAKE_INSTALL_PREFIX=/usr  \
               -DTESTDATADIR=$PWD/testfiles \
               -DENABLE_GLIB=ON \
               -DENABLE_UNSTABLE_API_ABI_HEADERS=ON     \
               {} \
               ".format("-DENABLE_LIBOPENJPEG='unmaintained' \
               -DENABLE_NSS3=OFF \
               -DENABLE_QT5=OFF \
               " if get.buildTYPE()=="emul32" else "")

    cmaketools.configure(options)

def build():
    shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig" if get.buildTYPE() == "emul32" else  "/usr/lib/pkgconfig" )

    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

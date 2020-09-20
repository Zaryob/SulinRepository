#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir="Vulkan-Loader-1.2.153"

def setup():
    if get.buildTYPE() == "emul32":
        shelltools.export("CC","gcc -m32")
        shelltools.export("CXX","g++ -m32")
        shelltools.export("LDFLAGS","-m32")
        cfg="-DCMAKE_INSTALL_LIBDIR=lib32"
    else:
        cfg="-DCMAKE_INSTALL_LIBDIR=lib"
    cmaketools.configure("--DCMAKE_INSTALL_PREFIX=/usr \
    -DVULKAN_HEADERS_INSTALL_DIR=/usr \
    -DCMAKE_INSTALL_SYSCONFDIR=/etc \
    -DCMAKE_INSTALL_DATADIR=/share \
    -DCMAKE_SKIP_RPATH=True \
    -DBUILD_TESTS=Off \
    -DBUILD_WSI_XCB_SUPPORT=On \
    -DBUILD_WSI_XLIB_SUPPORT=On \
    -DBUILD_WSI_WAYLAND_SUPPORT=On \
    -DCMAKE_BUILD_TYPE=Release "+cfg)

def build():
    cmaketools.make()

def install():
    cmaketools.install()

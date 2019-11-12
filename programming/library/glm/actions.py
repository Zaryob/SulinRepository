#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    cmaketools.configure("-DGLM_TEST_ENABLE=ON \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_INSTALL_LIBDIR=lib")

def build():
    cmaketools.make()

def install():
    #cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.dolib("glm/*.so")
    inarytools.dolib("glm/*.a")
    inarytools.insinto("/usr/include", "glm")
    inarytools.dodoc("readme.md", "copying.txt", "doc/manual.pdf")
    inarytools.dohtml("doc/*")

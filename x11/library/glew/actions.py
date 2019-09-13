#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def build():
    shelltools.system("sed -i 's|lib64|lib|' config/Makefile.linux")
    shelltools.system("sed -i '/^.PHONY: .*\.pc$/d' Makefile")
    
    if get.buildTYPE() == "emul32":
        inarytools.dosed("config/Makefile.linux", "LD = cc", "LD = gcc -m32")
        shelltools.system("sed -i 's|lib64|lib32|' config/Makefile.linux")
        autotools.make('CC="%s -m32" CXXFLAGS="%s"' % (get.CC(), get.CXXFLAGS()))
        return
    else:
        autotools.make('CC=%s CXXFLAGS="%s"' % (get.CC(), get.CXXFLAGS()))
        return

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("GLEW_DEST=%s/usr/ \
                              INCDIR=%s/emul32 \
                              BINDIR=%s/emul32 \
                              LIBDIR=%s/usr/lib32 \
                              PKGDIR=%s/usr/lib32/pkgconfig" % (get.installDIR() , get.installDIR(), get.installDIR(), get.installDIR(), get.installDIR()))

        inarytools.remove("/usr/lib32/libGLEW.a")
        inarytools.dosed("%s/usr/lib32/pkgconfig/glew.pc" % get.installDIR(), "/usr/lib", "/usr/lib32")
        return

    autotools.rawInstall("GLEW_DEST=%s/usr/ \
                          INCDIR=%s/usr/include/GL \
                          BINDIR=%s/usr/bin \
                          LIBDIR=%s/usr/lib" % (get.installDIR() , get.installDIR(), get.installDIR(), get.installDIR()))

    inarytools.dobin("bin/glewinfo")
    inarytools.dobin("bin/visualinfo")

    inarytools.dohtml("doc/*")
    inarytools.dodoc("README.md", "doc/*.txt", "LICENSE.txt")
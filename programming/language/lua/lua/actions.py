#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

major = ".".join(get.srcVERSION().split(".")[:2])

def setup():
    inarytools.dosed("src/Makefile", "^CFLAGS.*$", "CFLAGS=%s -fPIC -DLUA_USE_LINUX -DLUA_COMPAT_5_2 -DLUA_COMPAT_5_1" % get.CFLAGS())
    inarytools.dosed("src/Makefile", "^MYLDFLAGS.*$", "MYLDFLAGS=%s" % get.LDFLAGS())
    inarytools.dosed("lua.pc", "%VER%", "%s" % major)
    inarytools.dosed("lua.pc", "%REL%", "%s" % get.srcVERSION())

def build():
    autotools.make("linux")

def install():
    autotools.rawInstall("INSTALL_TOP=%s/usr INSTALL_MAN=%s/usr/share/man/ INSTALL_LIB=%s/usr/lib/" % (get.installDIR(), get.installDIR(), get.installDIR()))

    inarytools.insinto("/usr/lib", "src/liblua.so*")

    #free directory
    inarytools.removeDir("usr/lib/lua/")
    inarytools.removeDir("usr/share/lua/")

    inarytools.dohtml("doc")
    inarytools.dodoc("README")

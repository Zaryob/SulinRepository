#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools


def setup():
    options = "--with-pcre=system \
               --disable-fam \
               --disable-libelf \
               --enable-gtk-doc=no \
               --disable-libmount \
               --disable-static \
               --enable-shared \
               --disable-man \
               --enable-systemtap"


    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=/emul32/bin \
                     --sbindir=/emul32/sbin \
                     --disable-dtrace"
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

    #autotools.autoreconf("-vif")
    autotools.configure(options)

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        inarytools.domove("/usr/bin/gio-querymodules", "/usr/bin/32/")

    inarytools.removeDir("/usr/share/gdb")

    inarytools.dodoc("AUTHORS", "ChangeLog", "README", "NEWS")

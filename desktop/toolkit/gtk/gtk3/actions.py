#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools


def setup():
    options = "--prefix=/usr             \
               --sysconfdir=/etc         \
               --enable-x11-backend \
               --enable-broadway-backend \
               --disable-wayland-backend \
              "

    shelltools.export("CFLAGS", get.CFLAGS().replace("-fomit-frame-pointer",""))

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=/usr/bin32 \
                     --sbindir=/usr/sbin32 \
                     --enable-colord=no \
                   "

        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CC())
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS().replace("-fomit-frame-pointer",""))
        shelltools.export("CXXFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

        inarytools.dosed("configure.ac", "cups-config", "cups-config-32bit")

    autotools.autoreconf("-fiv")
    autotools.configure(options)

    inarytools.dosed("libtool", "( -shared )", r" -Wl,-O1,--as-needed\1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # remove empty dir
    inarytools.removeDir("/usr/share/man")
    inarytools.dodoc("AUTHORS", "README*", "HACKING", "ChangeLog*", "NEWS*")

    if get.buildTYPE() == "emul32":
        for binaries in ["gtk-query-immodules-3.0"]:
            inarytools.domove("/usr/bin/%s" % binaries, "/usr/bin/", "%s-32bit" % binaries)
        inarytools.removeDir("/usr/bin32")
#    inarytools.rename("/usr/bin/gtk3-update-icon-cache", "gtk3-update-icon-cache")

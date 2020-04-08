#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2015 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

suffix = "32" if get.buildTYPE() == "emul32" else ""

def setup():
    autotools.autoreconf("--install")
    #lfs udev rules
    autotools.configure("--sysconfdir=/etc \
		--with-rootprefix= \
		--with-rootrundir=/run \
		--with-rootlibexecdir=/lib/udev \
		--libdir=/usr/{} \
		--enable-split-usr \
		--enable-manpages \
		--disable-hwdb \
		--enable-kmod \
		--exec-prefix=/ \
		--bindir=/bin".format("lib{}".format("32" if get.buildTYPE() == "emul32" else "")))

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("-j1 DESTDIR=%s%s" % (get.installDIR(), suffix))
    # emul32 stop here
    if get.buildTYPE() == "emul32":
        shelltools.move("%s%s/usr/lib32" % (get.installDIR(), suffix), "%s/usr/lib32" % (get.installDIR()))
        for f in shelltools.ls("%s/usr/lib32/pkgconfig" % get.installDIR()):
            inarytools.dosed("%s/usr/lib32/pkgconfig/%s" % (get.installDIR(), f), "emul32", "usr")
    else:


        # Create /etc/udev/rules.d for backward compatibility
        inarytools.dodir("/etc/udev/rules.d")
        inarytools.dodir("/run/udev")

        # Add man files
        inarytools.doman("man/*.5", "man/*.7", "man/*.8")

        inarytools.dodoc("README*", "NOTES")

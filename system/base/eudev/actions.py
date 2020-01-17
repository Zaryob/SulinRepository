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
    autotools.configure("--prefix=/usr           \
                         --bindir=/sbin          \
                         --sbindir=/sbin         \
                         --libdir=/usr/{0}       \
                         --sysconfdir=/etc       \
                         --libexecdir=/{0}       \
                         --with-rootprefix=      \
                         --with-rootlibdir=/{0}  \
                         --enable-static         \
                         --disable-manpages ".format("lib{}".format("32" if get.buildTYPE() == "emul32" else "")))

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("-j1 DESTDIR=%s%s" % (get.installDIR(), suffix))
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # emul32 stop here
    if get.buildTYPE() == "emul32":
        shelltools.move("%s%s/lib32" % (get.installDIR(), suffix), "%s/lib32" % (get.installDIR()))
        shelltools.move("%s%s/usr/lib32" % (get.installDIR(), suffix), "%s/usr/lib32" % (get.installDIR()))
        for f in shelltools.ls("%s/usr/lib32/pkgconfig" % get.installDIR()):
            inarytools.dosed("%s/usr/lib32/pkgconfig/%s" % (get.installDIR(), f), "emul32", "usr")
        return

    #add link
    inarytools.dosym("/sbin/udevadm", "/bin/udevadm")

    # Create vol_id and scsi_id symlinks in /sbin probably needed by multipath-tools
    inarytools.dosym("/lib/udev/scsi_id", "/sbin/scsi_id")

    # Create /sbin/systemd-udevd -> /sbin/udevd sysmlink, we need it for MUDUR, do not touch this sysmlink.
    # inarytools.dosym("/lib/systemd/systemd-udevd", "/sbin/systemd-udevd")

    # Create /etc/udev/rules.d for backward compatibility
    inarytools.dodir("/etc/udev/rules.d")
    inarytools.dodir("/run/udev")

    # Add man files
    inarytools.doman("man/*.5", "man/*.7", "man/*.8")

    inarytools.dodoc("README*", "NOTES")

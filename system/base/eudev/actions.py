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
                         --libdir=/usr/lib       \
                         --sysconfdir=/etc       \
                         --libexecdir=/lib       \
                         --with-rootprefix=      \
                         --with-rootlibdir=/lib  \
                         --enable-static        \
                         --disable-manpages ")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("-j1 DESTDIR=%s%s" % (get.installDIR(), suffix))
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # emul32 stop here
    if get.buildTYPE() == "emul32":
        shelltools.move("%s%s/lib" % (get.installDIR(), suffix), "%s/lib%s" % (get.installDIR(), suffix))
        for f in shelltools.ls("%s/usr/lib/pkgconfig" % get.installDIR()):
            inarytools.dosed("%s/usr/lib/pkgconfig/%s" % (get.installDIR(), f), "emul32", "usr")
        shelltools.unlinkDir("%s%s" % (get.installDIR(), suffix))
        shelltools.unlink("%s32/usr/lib%s/libudev.so" % (get.installDIR(), suffix))
        inarytools.dosym("/lib%s/libudev.so.1.6.3" % suffix, "/usr/lib%s/libudev.so" % suffix)

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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools

def setup():
    shelltools.export("SYSTEMD_LIBD","-lelogind")
    shelltools.export("SYSTEMD_CFLAGS","-I/usr/include/elogind")
    autotools.autogen()
    autotools.configure("--without-plymouth    \
            --disable-static      \
            --enable-gdm-xsession \
            --with-pam-mod-dir=/lib/security\
            --with-systemdsystemunitdir=no")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.chown("%s/var/lib/gdm" % get.installDIR(), "gdm", "gdm")

    for d in ["/var/gdm", "/var/lib/gdm/.gconf*"]:
        inarytools.removeDir(d)

    for f in ["/var/lib/gdm/.gconf*", "/usr/sbin/gdm"]:
        inarytools.remove(f)

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")

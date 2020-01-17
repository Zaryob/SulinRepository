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
    autotools.autoreconf("-fi")

    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --sbindir=/usr/sbin \
                         --with-rundir=/run \
                         --libexecdir=/usr/libexec/ConsoleKit \
                         --localstatedir=/var \
                         --enable-polkit \
                         --enable-pam-module \
                         --enable-udev-acl \
                         --enable-docbook-docs \
                         --disable-static \
                         --with-dbus-services=/usr/share/dbus-1/services \
                         --with-logrotate-dir=/etc/logrotate.d \
                         --with-xinitrc-dir=/etc/X11/xinit/xinitrc.d \
                         --with-pam-module-dir=/lib/security \
                         --with-systemdsystemunitdir=no \
                         XMLTO_FLAGS='--skip-validation' \
                         ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s/" % get.installDIR())

    inarytools.removeDir("/run")

    inarytools.dodoc("AUTHORS", "README", "COPYING", "HACKING", "NEWS", "TODO")

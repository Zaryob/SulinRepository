#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import get
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools


def setup():
    autotools.configure("--prefix=/usr \
		--libexecdir=/usr/lib \
		--sbindir=/usr/bin \
		--sysconfdir=/etc \
		--localstatedir=/var \
		--with-dbus-config-dir=/usr/share/dbus-1/system.d \
		--with-priv-mode=setuid \
		--with-profile-dir=/etc/profile.d")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

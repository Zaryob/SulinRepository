#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--disable-static \
		--enable-introspection \
		--with-authfw=pam \
		--with-os-type=sulin \
		--disable-gtk-doc \
		--disable-gtk-doc-html \
		--disable-gtk-doc-pdf \
		--disable-libelogind \
		--disable-systemd \
		--disable-libsystemd-login")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s/" % get.installDIR())
    inarytools.dodir("/var/lib/polkit-1")

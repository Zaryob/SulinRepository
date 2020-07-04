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
    shelltools.system("  sed -i 's/have_png/use_png/g' configure.ac")
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--prefix=/usr \
		--sysconfdir=/etc \
		--localstatedir=/var \
		--enable-ft \
		--enable-gobject \
		--enable-pdf \
		--enable-png \
		--enable-ps \
		--enable-svg \
		--enable-tee \
		--enable-x \
		--enable-xcb \
		--enable-xcb-shm \
		--enable-xlib \
		--enable-xlib-xrender \
		--disable-xlib-xcb \
		--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #inarytools.removeDir("/usr/share/gtk-doc")
    #inarytools.dodoc("AUTHORS", "README", "ChangeLog", "NEWS", "COPYING", "COPYING-LGPL-2.1", "COPYING-MPL-1.1")

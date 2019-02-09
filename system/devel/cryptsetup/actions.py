#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--disable-static\
                         --sbindir=/sbin \
                         --libdir=/lib \
                         --disable-rpath \
                         --enable-python \
                         --with-python=/usr/bin/python3")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.domove("/lib/pkgconfig", "/usr/lib")
    inarytools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*",
                    "FAQ", "README*", "NEWS", "TODO")

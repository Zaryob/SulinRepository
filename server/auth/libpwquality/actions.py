#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import get
from inary.actionsapi import inarytools

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --with-securedir=/lib/security \
                         --disable-python-bindings \
                         --disable-static")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("ABOUT*", "AUTHORS", "ChangeLog", "COPYING", "README")

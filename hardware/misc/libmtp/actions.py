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
                         --disable-rpath \
                         --with-udev=/lib/udev \
                         --with-udev-rules=69-libmtp.rules")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #install HAL file for portable audio players
    inarytools.insinto("/usr/share/hal/fdi/information/10freedesktop", "libmtp.fdi", "10-usb-music-players-libmtp.fdi")

    inarytools.dodoc("ChangeLog", "COPYING", "README", "AUTHORS", "TODO")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir="thunar-4.16.0"

def setup():
    autotools.configure("--enable-gio-unix \
                         --enable-dbus \
                         --enable-startup-notification \
                         --enable-gudev \
                         --enable-notifications \
                         --enable-exif \
                         --enable-pcre \
                         --enable-debug")

    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "FAQ", "HACKING", "NEWS", "THANKS")

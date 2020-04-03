#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.autoreconf("-fiv")

    autotools.configure("--disable-static \
                         --disable-scrollkeeper \
                         --enable-djvu \
                         --enable-dvi \
                         --enable-comics \
                         --enable-t1lib \
                         --enable-nautilus \
                         --enable-introspection")
    inarytools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


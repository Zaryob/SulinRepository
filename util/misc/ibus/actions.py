#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools


def setup():
    #sandbox error fixed
    #inarytools.dosed("data/dconf/Makefile.am", "dconf update", "")
    #inarytools.dosed("data/dconf/Makefile.in", "dconf update", "")
    
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --libexecdir=/usr/lib/ibus \
                         --disable-gconf \
                         --disable-emoji-dict \
                         --enable-dconf \
                         --enable-wayland \
                         --enable-vala \
                         --enable-ui \
                         --enable-gtk-doc \
                         --enable-python-library \
                         --with-python=python3 \
                         --enable-gtk3 \
                         --enable-gtk2")
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

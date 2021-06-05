#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --libexecdir=/usr/lib \
                         --disable-static \
                         --enable-gio-unix \
                         --disable-gtk-doc")

def build():
    autotools.make()

def install():
    autotools.make("install DESTDIR={}".format(get.installDIR()))

    #legacy applet support
    inarytools.dosym("libxfce4panel-2.0.so","/usr/lib/libxfce4panel-1.0.so")
    inarytools.dosym("libxfce4panel-2.0.so","/usr/lib/libxfce4panel-1.0.so.4")

    #inarytools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    inarytools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "TODO")

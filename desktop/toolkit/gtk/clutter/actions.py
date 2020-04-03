#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

# WorkDir = ""
# NoStrip = "/"

def setup():
    autotools.configure(" --enable-introspection \
    --enable-egl-backend \
    --enable-gdk-backend \
    --enable-wayland-backend \
    --enable-x11-backend \
    --enable-evdev-input \
    --enable-wayland-compositor \
    --enable-gtk-doc ")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s INSTALL="install -p -c"' % get.installDIR())


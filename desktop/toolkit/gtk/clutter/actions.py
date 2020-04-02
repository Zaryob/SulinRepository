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

# WorkDir = ""
# NoStrip = "/"

def setup():
    autotools.configure("--enable-egl-backend\
            --enable-evdev-input ")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s INSTALL="install -p -c"' % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "README*", "NEWS")


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools

shelltools.export("CXXFLAGS","")
shelltools.export("CFLAGS","")
shelltools.export("LDFLAGS","")
    
def setup():
    shelltools.system("mkdir m4")
    shelltools.system("intltoolize")
    shelltools.system("autoreconf -fvi")
    autotools.configure("--prefix=/usr --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
    # fix conflict with gnome-themes
    inarytools.remove("usr/share/icons/HighContrast/index.theme")
    inarytools.remove("usr/share/themes/HighContrast/index.theme")
    inarytools.remove("usr/share/themes/HighContrast/gtk-2.0/gtkrc")

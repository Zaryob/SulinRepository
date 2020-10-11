#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    autotools.configure("--prefix=/usr \
                         --libexecdir=/usr/lib/xfce4 \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
    
    inarytools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    inarytools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README")

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
                         --libexecdir=/usr/lib/xfce4 \
                         --disable-static \
                         --disable-gtk-doc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #legacy support
    inarytools.dosym("libexo-2.so","/usr/lib/libexo-1.so")
    inarytools.dosym("libexo-2.so.0","/usr/lib/libexo-1.so.0")

    inarytools.dodoc("AUTHORS", "COPYING*", "ChangeLog", "NEWS", "THANKS")

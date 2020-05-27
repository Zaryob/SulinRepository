#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --libexecdir=/usr/lib/cinnamon-settings-daemon \
                         --localstatedir=/var \
                         --disable-static \
                         --disable-systemd")
    
    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    shelltools.system("make")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("COPYING", "AUTHORS")

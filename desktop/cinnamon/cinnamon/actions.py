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
    shelltools.system("./autogen.sh")
    autotools.configure("--localstatedir=/var \
                         --libexecdir=/usr/lib/cinnamon \
                         --prefix=/usr \
                         --sysconfdir=/etc \
                         --disable-schemas-install \
                         --enable-compile-warnings=yes \
                         --enable-gtk-doc")
    
    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    

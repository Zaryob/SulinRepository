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
                         --localstatedir=/var \
                         --disable-static \
                         --disable-rpath \
                         --disable-caja \
                         --enable-pdf \
                         --enable-tiff \
                         --enable-djvu \
                         --enable-dvi \
                         --enable-xps \
                         --enable-t1lib \
                         --enable-comics \
                         --enable-pixbuf \
                         --enable-impress \
                         --with-gtk=3.0 ")
    
    # for fix unused dependency
    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    inarytools.dodoc("README", "NEWS", "AUTHORS", "COPYING")

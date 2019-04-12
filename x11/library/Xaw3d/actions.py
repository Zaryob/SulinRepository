#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--prefix=/usr \
                         --disable-static \
                         --enable-arrow-scrollbars \
                         --enable-gray-stipples \
                         --enable-multiplane-bitmaps")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    inarytools.dodoc("ChangeLog","COPYING","README","src/README.XAW3D")

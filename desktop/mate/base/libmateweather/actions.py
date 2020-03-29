#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--disable-static       \
                         --with-gnu-ld          \
                            --with-gtk3 \
			                --enable-locations-compression \
                         --enable-gtk-doc-html")
    
    # fix unused-direct-shlib-dependency
    inarytools.dosed("libtool", "( -shared )", " -Wl,-O1,--as-needed\\1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

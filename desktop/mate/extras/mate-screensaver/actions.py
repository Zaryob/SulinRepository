#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure(" --enable-locking \
                          --with-xf86gamma-ext \
                          --with-kbd-layout-indicator \
                          --with-systemd=no \
                          --prefix=/usr \
                          --sysconfdir=/etc \
                          --without-console-kit \
                          --with-xscreensaverdir=/usr/share/xscreensaver/config \
                          --with-xscreensaverhackdir=/usr/lib/misc/xscreensaver")
    
    # for fix unused dependency
    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # remove needless gsettings convert file to avoid slow session start
    

    inarytools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS", "COPYING")

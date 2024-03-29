#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    options = "--with-glib=yes \
               --with-freetype=yes \
               --with-cairo=yes \
               --with-icu=yes \
               --with-gobject=yes \
               --with-graphite2=yes"

    if get.buildTYPE() == "emul32":
        options += "--with-glib=yes \
                    --with-graphite2=no \
                    --with-cairo=yes \
                    --with-icu=yes"
    autotools.configure(options)

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

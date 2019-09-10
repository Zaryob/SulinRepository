#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    autotools.configure("\
                         --disable-static \
                         --enable-experimental \
                         --enable-libwebpdecoder \
                         --enable-libwebpdemux \
                         --enable-libwebpmux \
                         --enable-swap-16bit-csp \
                        ")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ") 

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


    inarytools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "PATENTS", "README")
    #shelltools.move("%s/libwebp-0.2.1/doc/*" % get.workDIR(),"%s/usr/share/doc/webp" % get.installDIR())
    #shelltools.move("%s/libwebp-0.2.1/README" % get.workDIR(),"%s/usr/share/doc/webp" % get.installDIR())

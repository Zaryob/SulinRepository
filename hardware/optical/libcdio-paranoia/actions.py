#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    inarytools.dosed("configure.ac", "AM_CONFIG_HEADER", "AC_CONFIG_HEADERS")
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --disable-example-progs \
                         --enable-cpp-progs \
                         --with-cd-paranoia-name=libcdio-paranoia")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("-j1 DESTDIR=%s" % (get.installDIR()))

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README*", "THANKS")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import autotools
from inary.actionsapi import get

def setup():
    inarytools.dosed("configure.ac", "-O3", "")
    shelltools.export("CPPFLAGS", get.CXXFLAGS())

    shelltools.system("./bootstrap")
    autotools.configure("--disable-static \
                         --disable-ecore \
                         --enable-glib")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "README", "COPYING")

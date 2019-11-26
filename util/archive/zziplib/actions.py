#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --enable-sdl \
                         --with-zlib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for manp in shelltools.ls("man3"):
        inarytools.doman("man3/%s" % manp)

    inarytools.dohtml("docs/*.htm*")
    inarytools.dodoc("ChangeLog", "COPYING.LIB", "README", "TODO", "docs/COPYING*", "docs/README.SDL")

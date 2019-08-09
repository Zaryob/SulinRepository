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
    shelltools.system("sed -i '/math.h/a #include <malloc.h>' src/flexdef.h")
    inarytools.flags.add("-fPIC")
    shelltools.export("AUTOPOINT", "true")

    autotools.autoreconf("-vfi")
    # do not enable nls http://bugs.gentoo.org/121408
    autotools.configure("--disable-nls \
                         --disable-dependency-tracking")
    
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dosym("flex", "/usr/bin/lex")

    inarytools.dodoc("NEWS", "README.md")

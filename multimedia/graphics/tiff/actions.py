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
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --without-x \
                         --enable-cxx \
                         --with-pic")
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32": return

    inarytools.rename("/%s/tiff-%s" % (get.docDIR(), get.srcVERSION()), get.srcNAME())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import libtools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    # libtools.libtoolize("--force --install")
    autotools.configure("--disable-dependency-tracking \
                         --enable-alsa \
                         --enable-alsa-mmap \
                         --enable-pulse \
                         --disable-arts \
                         --disable-esd \
                         --disable-nas \
                         --enable-shared \
                         --disable-static")
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.removeDir("/usr/share/doc")

    inarytools.dohtml("doc/*")
    inarytools.dodoc("AUTHORS", "CHANGES", "README", "TODO")

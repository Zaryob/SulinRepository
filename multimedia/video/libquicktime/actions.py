#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import libtools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools


NoStrip = "/"
KeepSpecial = ["libtool"]

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")

    autotools.configure("--enable-shared \
                         --enable-asm \
                         --enable-gpl \
                         --with-alsa \
                         --with-faad2 \
                         --with-ffmpeg \
                         --with-lame \
                         --with-libdv \
                         --with-libjpeg \
                         --with-libpng \
                         --with-opengl \
                         --with-schroedinger \
                         --with-x \
                         --with-x264 \
                         --without-doxygen \
                         --without-cpuflags")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.remove("/usr/lib/libquicktime.la")

    inarytools.dodoc("README", "TODO", "ChangeLog")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Suleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir = "mjpegtools-%s" % get.srcVERSION().replace("_", "")

def setup():
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())
    autotools.autoreconf("-vfi")

    inarytools.dosed("configure", "ARCHFLAGS=.*", "ARCHFLAGS=")
    autotools.configure("--with-x \
                         --enable-largefile \
                         --enable-simd-accel \
                         --with-dv-yv12 \
                         --disable-static \
                         --with-libpng \
                         --with-libdv=/usr")


def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("AUTHORS","ChangeLog","README*","mjpeg_howto.txt", "TODO")

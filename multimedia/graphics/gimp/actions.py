#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Süleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    #autotools.autoreconf("-fi")
    autotools.configure("--without-webkit \
                         --disable-gtk-doc \
                         --disable-altivec \
                         --disable-alsatest \
                         --enable-python \
                         --enable-default-binary \
                         --enable-mmx \
                         --enable-sse \
                         --enable-mp \
                         --with-linux-input \
                         --with-poppler \
                         --with-libjpeg \
                         --with-libexif \
                         --with-librsvg \
                         --with-libtiff \
                         --with-libmng \
                         --with-libpng \
                         --disable-python \
                         --with-webkit \
                         --with-lcms \
                         --with-alsa \
                         --with-dbus \
                         --with-aa \
                         --with-x")

    # Add illustrator and other mime types
    inarytools.dosed("desktop/gimp.desktop.in", "^MimeType=application/postscript;application/pdf;(.*)$",
                    "MimeType=\\1;image/x-sun-raster;image/x-gray;image/x-pcx;image/jpg;image/x-bmp;image/pjpeg;image/x-png;application/illustrator;")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog*", "HACKING", "NEWS", "README", "INSTALL", "LICENSE")

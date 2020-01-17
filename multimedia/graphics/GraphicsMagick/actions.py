#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import perlmodules
from inary.actionsapi import get

# .la files needed to load modules
KeepSpecial = ["libtool"]

def setup():
    # ghostscript is better than dps
    # unstable fpx support disabled
    # trio is for old systems not providing vsnprintf
    autotools.configure("--enable-openmp \
                         --enable-shared \
                         --disable-static \
                         --disable-openmp \
                         --with-threads \
                         --with-modules \
                         --with-magick-plus-plus \
                         --with-perl \
                         --with-bzlib \
                         --without-dps \
                         --without-fpx \
                         --with-gslib \
                         --with-jbig \
                         --with-jpeg \
                         --with-jp2 \
                         --with-lcms \
                         --with-png \
                         --with-tiff \
                         --without-trio \
                         --with-ttf \
                         --with-wmf \
                         --with-fontpath=/usr/share/fonts \
                         --with-gs-font-dir=/usr/share/fonts/default/ghostscript \
                         --with-xml \
                         --with-zlib \
                         --with-x \
                         --with-quantum-depth=16")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()
    autotools.make("perl-build")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s -C PerlMagick" % get.installDIR())
    for d in ("demo/", "Changelog", "README.txt"):
        inarytools.insinto("/usr/share/doc/PerlMagick", "PerlMagick/%s" % d)

    inarytools.remove("/usr/lib/*.la")
    perlmodules.removePacklist()
    perlmodules.removePodfiles()

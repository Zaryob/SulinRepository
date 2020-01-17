#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import perlmodules
from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

KeepSpecial=["libtool"]

def setup():
    inarytools.dosed("configure.ac", "AC_PATH_XTRA")
    autotools.autoreconf("-fi")

    inarytools.dosed("configure", "DOCUMENTATION_RELATIVE_PATH=.*", "DOCUMENTATION_RELATIVE_PATH=%s/html" % get.srcNAME())
    autotools.configure("--with-dejavu-font-dir=/usr/share/fonts/TTF \
                         --with-gs-font-dir=/usr/share/fonts/default/ghostscript \
                         --docdir=/usr/share/doc/imagemagick \
                         PSDelegate=/usr/bin/gs \
                         XPSDelegate=/usr/bin/gxps \
                         PCLDelegate=/usr/bin/gpcl6 \
                         --enable-hdri \
                         --enable-shared \
                         --enable-opencl \
                         --disable-static \
                         --with-modules \
                         --with-perl \
                         --with-openexr \
                         --with-openjp2 \
                         --with-perl-options='INSTALLDIRS=vendor' \
                         --with-x \
                         --with-threads \
                         --with-magick_plus_plus \
                         --with-gslib \
                         --with-wmf \
                         --with-lcms2 \
                         --with-rsvg \
                         --with-xml \
                         --with-djvu \
                         --with-bzlib \
                         --with-zlib \
                         --with-fpx \
                         --with-tiff \
                         --with-jp2 \
                         --with-jpeg \
                         --without-jbig \
                         --without-gcc-arch \
                         --without-gvc  \
                         --without-fpx \
                         --without-dps")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS.txt", "ChangeLog", "LICENSE", "NEWS.txt")

    inarytools.remove("/usr/lib/*.la")

    perlmodules.removePacklist()
    perlmodules.removePodfiles()

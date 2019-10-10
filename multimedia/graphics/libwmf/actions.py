#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import autotools

def setup():
    shelltools.unlink("configure.in")
    inarytools.dosed("Makefile.am","doc","")
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-gd \
                         --disable-static \
                         --with-freetype \
                         --with-jpeg \
                         --with-layers \
                         --with-png \
                         --with-sys-gd \
                         --with-zlib \
                         --with-gsfontdir=/usr/share/fonts/default/ghostscript \
                         --with-fontdir=/usr/share/libwmf/fonts \
                         --with-docdir=/usr/share/doc/%s" % get.srcNAME() )
def build():
    autotools.make()

def install():
    inarytools.dosed("fonts/fontmap", "libwmf/fonts", "fonts/default/ghostscript")

    autotools.rawInstall("DESTDIR=%s \
                          fontdir=/usr/share/libwmf/fonts \
                          wmfonedocdir=/usr/share/doc/%s/caolan \
                          wmfdocdir=/usr/share/doc/%s" %
                          ( get.installDIR(), get.srcNAME(), get.srcNAME() ) )

    inarytools.dodoc("README", "AUTHORS", "CREDITS", "ChangeLog", "NEWS", "TODO")

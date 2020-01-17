#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import libtools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    inarytools.dosed("source/SoundStretch/Makefile.*", "-O3", "")
    shelltools.system("sed -i 's/AM_CONFIG_HEADER/AC_CONFIG_HEADER/' configure.ac")
    shelltools.system("./bootstrap")
    autotools.configure("--enable-shared \
                         --disable-dependency-tracking \
                         --disable-static \
                         --disable-integer-samples \
                         --with-pic")

    # Avoid rpath
    inarytools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    inarytools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s pkgdocdir=/usr/share/doc/%s" % (get.installDIR(), get.srcNAME()))

    # Install compat symlinks for pkgconfig files
    inarytools.dosym("/usr/lib/pkgconfig/soundtouch.pc", "/usr/lib/pkgconfig/soundtouch-1.4.pc")
    inarytools.dosym("/usr/lib/pkgconfig/soundtouch.pc", "/usr/lib/pkgconfig/SoundTouch-1.0.pc")
    inarytools.dosym("/usr/lib/pkgconfig/soundtouch.pc", "/usr/lib/pkgconfig/SoundTouch-1.4.pc")

    # Install docs
    inarytools.dodoc("COPYING.TXT", "README.html")

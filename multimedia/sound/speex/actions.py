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
    shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=64" % get.CFLAGS())

    inarytools.dosed("libspeex/Makefile.am", "noinst_PROGRAMS", "check_PROGRAMS")

    options = "--enable-ogg \
               --enable-sse \
               --disable-static"

    if get.buildTYPE() == "emul32":
        # ogg only affects the executables so it's safe to disable for emul32
        options += " --libdir=/usr/lib32 --disable-ogg"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.autoreconf("-vif")
    autotools.configure(options)

    # Remove rpath from speexenc and speexdec
    inarytools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    inarytools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s docdir=/usr/share/doc/speex" % get.installDIR())

    inarytools.dodoc("README")

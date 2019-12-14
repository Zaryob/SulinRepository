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
    autotools.configure("--disable-static \
                         --disable-dependency-tracking \
                         --enable-fast-install \
                         --enable-debugalloc \
                         %s" % ("--enable-frame-pointers" if get.ARCH() == "x86_64" else ""))

    # Disable rpath
    inarytools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    inarytools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("noinst_PROGRAMS=' '")

def install():
    autotools.rawInstall("DESTDIR=%s docdir=/usr/share/doc/gperftools" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")

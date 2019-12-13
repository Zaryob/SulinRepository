#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    autotools.configure("--prefix=/usr \
                         --libexecdir=/usr/lib \
                         --disable-static \
                         --enable-gio-unix \
                         --disable-gtk-doc \
                         --enable-debug")

    inarytools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    inarytools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    inarytools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README", "TODO")

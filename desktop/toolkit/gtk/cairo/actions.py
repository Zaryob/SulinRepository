#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    inarytools.flags.add("-flto -ffat-lto-objects")
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --enable-xlib \
                         --disable-drm \
                         --enable-xml \
                         --enable-ft \
                         --enable-ps \
                         --enable-pdf \
                         --enable-svg \
                         --enable-tee \
                         --enable-gl \
                         --enable-gobject \
                         --disable-gtk-doc")

    inarytools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    inarytools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.removeDir("/usr/share/gtk-doc")
    inarytools.dodoc("AUTHORS", "README", "ChangeLog", "NEWS", "COPYING", "COPYING-LGPL-2.1", "COPYING-MPL-1.1")

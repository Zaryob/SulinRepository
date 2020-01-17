#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--disable-static")
    inarytools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")
    inarytools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    inarytools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.install()

    dirs = ["/usr/share/doc", "/usr/share/devhelp"]
    for dir in dirs:
        inarytools.removeDir(dir)

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")

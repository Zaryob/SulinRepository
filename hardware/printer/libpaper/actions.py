#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.configure('--disable-static')

    # Disable rpath
    inarytools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    inarytools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.install()

    for lang in shelltools.ls("debian/po/*.po"):
        inarytools.domo(lang, shelltools.baseName(lang).replace(".po", ""), "libpaper.mo")

    inarytools.dodoc("README", "ChangeLog")

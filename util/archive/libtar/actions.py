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
    #libtar-1.2.11-free.patch
    inarytools.dosed("lib/output.c", "#ifdef STDC_HEADERS", "#ifdef STDC_HEADERS\n# include <stdlib.h>")
    inarytools.dosed("lib/wrapper.c", "#ifdef STDC_HEADERS", "#ifdef STDC_HEADERS\n# include <stdlib.h>")
    autotools.autoreconf("-fvi")
    autotools.configure("--disable-static")

    # Remove rpath
    inarytools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    inarytools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("ChangeLog*", "COPYRIGHT", "README", "TODO")

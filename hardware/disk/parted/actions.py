#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import libtools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    inarytools.flags.add("-Wno-unused-but-set-variable")
    autotools.autoreconf()
    autotools.autoconf()

    autotools.configure("--disable-static \
                         --disable-gcc-warnings")
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    inarytools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")


def build():
    autotools.make("V=1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
    inarytools.dodoc("doc/API", "doc/USER.jp", "doc/FAT")


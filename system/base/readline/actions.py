#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    shelltools.system("sed -i '/MV.*old/d' Makefile.in")
    shelltools.system("sed -i '/{OLDSUFF}/c:' support/shlib-install")
    inarytools.cflags.add("-fPIC")

    #Force link to ncurses instead of tinfo, which we don't have, will be needed when we use as-needed ;)
    inarytools.dosed("support/shobj-conf", "^(SHLIB_LIBS=)", "\\1-lncurses")

    inarytools.dosed("support/shobj-conf", "\-Wl,\-rpath,\$\(libdir\)\s")
    autotools.configure("--with-curses \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    if get.buildTYPE() == "emul32": return

    inarytools.removeDir("/usr/bin")

    inarytools.dohtml("doc/")
    inarytools.dodoc("CHANGELOG", "CHANGES", "README", "USAGE", "NEWS")

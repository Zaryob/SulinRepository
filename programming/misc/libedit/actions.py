#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --enable-widec \
                         --disable-dependency-tracking \
                         --enable-fast-install")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE()=="emul32":
        inarytools.remove("/usr/lib32/libedit.la")
        return


    inarytools.dodoc("ChangeLog", "COPYING", "THANKS")
    inarytools.remove("/usr/lib/libedit.la")
    inarytools.remove("/usr/share/man/man3/history.3")

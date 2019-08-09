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
                         --enable-libgdbm-compat")

def build():
    autotools.make("prefix=/usr")

def install():
    autotools.install("prefix=%s/usr" % get.installDIR())

    inarytools.dosym("../gdbm.h", "/usr/include/gdbm/gdbm.h")
    inarytools.dosym("../dbm.h", "/usr/include/gdbm/dbm.h")
    inarytools.dosym("../ndbm.h", "/usr/include/gdbm/ndbm.h")

    inarytools.dodoc("ChangeLog", "NEWS", "README")

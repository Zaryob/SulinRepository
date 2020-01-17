#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    if get.buildTYPE() != "emul32":
        inarytools.flags.add("-fPIC")

    autotools.configure("--disable-static \
                         --with-gmp")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("CFLAGS=-O2 LDFLAGS=-s")

def install():
    autotools.install()

    inarytools.dodoc("README", "ChangeLog", "NEWS", "COPYING", "AUTHORS")


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    autotools.make("CC=%s CFLAGS='%s -fPIC' LDFLAGS='%s'" % (get.CC(), get.CFLAGS(), get.LDFLAGS()))

def install():
    inarytools.dolib("libiniparser.so.1")
    inarytools.dosym("libiniparser.so.1", "/usr/lib/libiniparser.so")

    inarytools.dodir("/usr/include")
    inarytools.insinto("/usr/include", "src/*.h")

    inarytools.dodoc("README.md", "AUTHORS", "LICENSE")

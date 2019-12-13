#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir="lwlocate-0.1/master"

def build():
    autotools.make("-f Makelib")
    autotools.make()

def install():
    inarytools.insinto("/usr/lib", "libwlocate.so")
    inarytools.insinto("/usr/include", "libwlocate.h")
    inarytools.insinto("/usr/bin", "lwtrace")

    inarytools.dodoc("COPYING", "README", "CREDITS")

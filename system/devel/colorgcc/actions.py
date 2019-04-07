#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get


def install():
    inarytools.dobin("colorgcc")
    inarytools.insinto("/etc", "colorgccrc")

    inarytools.dodir("/usr/share/colorgcc")
    inarytools.dosym("/usr/bin/colorgcc", "/usr/share/colorgcc/colorgcc")

    for c in ["gcc", "cc", "g++", "c++", "gfortran", "gcj", get.CC(), get.CXX()]:
        inarytools.dosym("/usr/share/colorgcc/colorgcc", "/usr/share/colorgcc/%s" % c)

    inarytools.dodoc("COPYING", "ChangeLog", "CREDITS")

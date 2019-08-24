#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    autotools.make("-f unix/Makefile CC=%s CPP=%s generic_gcc" % (get.CC(), get.CXX()))

def install():
    for bin in ["zip","zipcloak","zipnote","zipsplit"]:
        inarytools.dobin(bin)

    inarytools.doman("man/*.1")
    inarytools.dodoc("BUGS", "CHANGES", "LICENSE", "README", "TODO", "WHATSNEW", "WHERE")

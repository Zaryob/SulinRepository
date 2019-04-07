#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "%s+-%s" % (get.srcNAME(), get.srcVERSION())
docompile = False if get.ARCH() == "x86_64" else True

def setup():
    inarytools.dosed("memtest.lds", "0x5000", "0x100000")

def build():
    if docompile:
        autotools.make()

def install():
    if docompile:
        finalbin = "memtest.bin"
    else:
        finalbin = "precomp.bin"

    inarytools.insinto("/boot", finalbin, "memtest")

    inarytools.dodoc("FAQ", "README*")


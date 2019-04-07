#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def build():
    shelltools.chmod("build_detect_platform", 0o755)
    autotools.make()

def check():
    autotools.make("check")

def install():
    inarytools.dolib("libleveldb.so.1.18")
    inarytools.dosym("libleveldb.so.1.18", "/usr/lib/libleveldb.so.1")
    inarytools.dosym("libleveldb.so.1.18", "/usr/lib/libleveldb.so")

    inarytools.insinto("/usr/include", "include/*")
    inarytools.insinto("/usr/include", "helpers/memenv/memenv.h")

    inarytools.dodoc("README", "LICENSE", "NEWS", "AUTHORS")

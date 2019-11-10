#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    cmaketools.configure("-DBUILD_SHARED_LIBS=1")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.insinto("/usr/include", "include/*")
    inarytools.insinto("/usr/include", "helpers/memenv/memenv.h")

    inarytools.dodoc("README.md", "LICENSE", "NEWS", "AUTHORS")

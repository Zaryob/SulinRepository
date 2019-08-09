#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import cmaketools
from inary.actionsapi import get
from inary.actionsapi import inarytools

def setup():
    cmaketools.configure("-DWITH_JPEG8=1 ")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32": return

    # provide jpegint.h as it is required by various software
    inarytools.insinto("/usr/lib/include", "jpegint.h")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        inarytools.removeDir("/usr/lib32/%s" % get.srcDIR())
        inarytools.dosym("/usr/lib/%s/include" % get.srcDIR(),
        "/usr/lib32/%s/include" % get.srcDIR())

    inarytools.dodoc("ChangeLog*", "LICENSE", "README*")

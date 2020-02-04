#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools

def setup():
    options = "--disable-static"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
    inarytools.dosed("Makefile.in","check: scripts/symbols.chk","check:")
    autotools.configure(options)

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        inarytools.remove("/usr/lib32/libpng.la")
        shelltools.system("rm -f {}/usr/lib32/libpng.so*".format(get.installDIR()))
    else:
        inarytools.remove("/usr/lib/libpng.la")
        shelltools.system("rm -f {}/usr/lib/libpng.so*".format(get.installDIR()))
    inarytools.dodoc("ANNOUNCE", "CHANGES", "README", "TODO")

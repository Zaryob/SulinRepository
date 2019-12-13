#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools

WorkDir="gsm-gsm-1.0-pl13"

def setup():
    multilib = " -m32" if get.buildTYPE() == "emul32" else ""
    inarytools.dosed("Makefile", "sulinCC", "%s %s" % (get.CC(), multilib))
    inarytools.dosed("Makefile", "sulinCFLAGS", "%s %s" % (get.CFLAGS(), multilib))

def build():
    autotools.make()

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("DESTDIR=%s bindir=/emul32 libdir=/usr/lib32" % get.installDIR())
        inarytools.remove("/usr/lib32/libgsm.a")
        return
    else:
        autotools.rawInstall("DESTDIR=%s bindir=/usr/bin" % get.installDIR())

    for bin in ["tcat","untoast"]:
        inarytools.remove("/usr/bin/%s" % bin)
        inarytools.dosym("toast", "/usr/bin/%s" % bin)

    # Move gsm.h out of gsm subdir
    # inarytools.insinto("/usr/include","inc/gsm.h")
    # inarytools.removeDir("/usr/include/gsm")

    # No static libs
    inarytools.remove("/usr/lib/libgsm.a")

    inarytools.dodoc("ChangeLog", "COPYRIGHT", "MACHINES", "MANIFEST", "README")

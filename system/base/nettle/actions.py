#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import get
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools


def setup():
    options = "--enable-shared"

    if not get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib"

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        #inarytools.remove("/usr/lib32/*.a")
        return

    #inarytools.remove("/usr/lib/*.a")
    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "README", "nettle.pdf")

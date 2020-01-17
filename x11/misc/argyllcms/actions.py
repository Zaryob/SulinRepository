#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    shelltools.system("./legal.sh")
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static")

    # for fix unused dependency
    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=" + get.installDIR())

    inarytools.dodoc("AUTHORS", "NEWS", "ChangeLog", "COPYING", "README")

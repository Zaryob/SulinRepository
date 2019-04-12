#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--disable-static")
    inarytools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.domove("/usr/share/doc/%s-1.6/*" % get.srcNAME(), "/usr/share/gtk-doc/html/atkmm")
    inarytools.removeDir("/usr/share/doc/%s-1.6" % get.srcNAME())
    inarytools.removeDir("/usr/share/devhelp")

    inarytools.dodoc("ChangeLog", "COPYING", "NEWS", "README")

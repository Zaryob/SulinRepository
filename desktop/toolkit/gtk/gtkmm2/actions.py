#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    shelltools.export("CFLAGS","")
    shelltools.export("CXXFLAGS","")
    shelltools.export("LDFLAGS","")
    autotools.configure("--disable-docs")

def build():
    autotools.make()

def install():
    autotools.install()

    #inarytools.removeDir("/usr/share/gtkmm-2.4")
    inarytools.removeDir("/usr/share/devhelp")

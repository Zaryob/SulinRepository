#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    # dont waste time building examples, docs and tests
    shelltools.system("sed -e '/^libdocdir =/ s/$(book_name)/libsigc++-2.10.2/' -i docs/Makefile.in")
    
    autotools.configure("--disable-static")

    inarytools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.removeDir("/usr/share/devhelp")

    inarytools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")

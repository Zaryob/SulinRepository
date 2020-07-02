#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

def setup():
    #shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--disable-schemas-compile --enable-compile-warnings=minimum --enable-gtk-doc --disable-eds")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")

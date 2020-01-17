#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():

    autotools.configure("--without-python --with-python3")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    shelltools.export("CFLAGS", get.CFLAGS()+"  $(python3-config --includes)")
    shelltools.export("CXXFLAGS", get.CXXFLAGS()+"  $(python3-config --includes)")

    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

shelltools.export("CXXFLAGS","")
shelltools.export("LDFLAGS","")
shelltools.export("CFLAGS","")
    
def setup():
    autotools.configure("--enable-animation --enable-lua --with-system-lua")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("ChangeLog", "COPYING", "NEWS", "README")

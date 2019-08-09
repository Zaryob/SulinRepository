#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-shared \
                         --disable-static\
                         --with-x")
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    
def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "TODO")


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
    autotools.autoreconf("-fi")

    autotools.configure("--disable-dependency-tracking \
                --disable-static --with-extra-only")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()
    autotools.make()

def install():
    autotools.install()
    inarytools.dodoc("AUTHORS", "COPYING", "TODO")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    #autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --enable-shared")
                         
def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("COPYING", "README", "ChangeLog", "AUTHORS", "NEWS")

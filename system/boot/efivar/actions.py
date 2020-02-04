#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    autotools.make("libdir=/usr/lib bindir=/usr/bin includedir=/usr/include/ V=1 -j1")

def install():
     autotools.rawInstall("DESTDIR=%s libdir=/usr/lib/" % get.installDIR())

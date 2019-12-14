#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# nut is done with checkouts from
# svn://svn.mplayerhq.hu/nut/src/trunk

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def build():
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())
    autotools.make("-j1 CC=%s" % get.CC())

def install():
    autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())

    inarytools.dodoc("COPYING", "README*")

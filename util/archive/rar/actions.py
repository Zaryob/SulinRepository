#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "%s/%s" % (get.ARCH(), get.srcNAME())
NoStrip = ["/"]

def install():
    inarytools.insinto("/opt/rar/bin", "rar")
    inarytools.insinto("/opt/rar/lib", "default.sfx")
    inarytools.insinto("/opt/rar/etc", "rarfiles.lst")

    inarytools.dosym("/opt/rar/bin/rar", "/usr/bin/rar")

    inarytools.dodoc("license.txt", "readme.txt", "whatsnew.txt", "order.htm", "rar.txt")

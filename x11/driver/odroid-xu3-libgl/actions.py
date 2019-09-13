#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    shelltools.system("git clone git://github.com/mdrjr/5422_mali")

def install():
    
    shelltools.cd("5422_mali")
    
    inarytools.insinto("/usr/lib/mali-egl", "x11/*")
   # inarytools.insinto("/usr/lib/mali-egl", "fbdev/*")
    inarytools.insinto("/usr/include", "headers/CL*")
    inarytools.dodoc("LICENSE.md")

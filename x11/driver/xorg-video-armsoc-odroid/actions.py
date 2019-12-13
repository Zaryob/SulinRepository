#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

WorkDir="xf86-video-armsoc-0.6.0-1endless9"

def setup():
    shelltools.system("sh autogen.sh --prefix=/usr --with-drmmode=exynos")
    #autotools.configure("--with-drmmode=exynos")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
  #  inarytools.dodoc("NEWS", "README")



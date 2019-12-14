#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

#WorkDir = "flite-%s-current" % get.srcVERSION()
   
def setup(): 
    autotools.configure("--prefix=/usr \
                         --with-audio=alsa \
                         --with-vox=cmu_us_kal16")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("COPYING", "README")

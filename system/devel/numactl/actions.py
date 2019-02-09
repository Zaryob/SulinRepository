#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")    
    autotools.configure("--prefix=/usr")
      
    
def build():
    autotools.make("CFLAGS='%s -I.'" % get.CFLAGS())

def install():
    autotools.install()

    inarytools.remove("/usr/lib/*.a")
    inarytools.removeDir("/usr/share/man/man2")

    inarytools.dodoc("CHANGES", "DESIGN")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr ")

def build():
    autotools.make()

def install():
    autotools.install()
    #inarytools.dobin("mkfs/mkexfatfs")
    #inarytools.dobin("dump/dumpexfat")
    #inarytools.dobin("fsck/exfatfsck")
    #inarytools.dobin("label/exfatlabel")    
    
    #inarytools.doman("mkfs/mkexfatfs.8")
    #inarytools.doman("dump/dumpexfat.8")
    #inarytools.doman("fsck/exfatfsck.8")
    #inarytools.doman("label/exfatlabel.8")
    
    inarytools.dodoc("ChangeLog", "COPYING", "README")
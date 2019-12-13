#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.system("./autogen.sh")
    
    autotools.configure("--prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # move docs into proper place
    #inarytools.domove("/usr/share/libatomic_ops/", "/usr/share/doc/%s" % get.srcNAME())

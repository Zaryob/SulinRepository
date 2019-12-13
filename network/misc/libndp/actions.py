#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools


def setup():
    shelltools.system("sh autogen.sh")
    
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --disable-static \
                         --libexecdir=/usr/lib")

def build():
    autotools.make()

#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.dodoc("COPYING", "README")

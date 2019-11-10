#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get

#optimizationtype = "--enable-amd64" if get.ARCH() == "x86_64", "--enable-asd" if get.ARCH() == "armv7h" else "--enable-mmx"


if get.ARCH() == 'x86_64':
       optimizationtype = " --enable-amd64"
       
elif get.ARCH() == 'armv7h':
       optimizationtype = " "
        
else:
    optimizationtype = " --enable-mmx"

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                                      --prefix=/usr \
                                      --sysconfdir=/etc/imlib2 \
                                      --x-libraries=/usr/lib")
     
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dohtml("doc/*")
    inarytools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")

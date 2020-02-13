#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    shelltools.system(" ./configure --prefix=/usr --sysconfdir=/etc \
                          --libdir=/usr/lib \
                          --enable-svgz --disable-gtk-doc")
       
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import get
from inary.actionsapi import shelltools

def setup():
  #  shelltools.export("MOC5", "moc-qt5")
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--disable-tests \
		--enable-vala \
		--with-greeter-session=lightdm-gtk-greeter \
                 --with-greeter-user='root' ")
    
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


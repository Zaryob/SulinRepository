#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--enable-gtk --enable-buildin-clipboard \
    --enable-buildin-polkit")

def build():
    autotools.make()

def install():
    autotools.install()
    #lxpolkit only start with lxde
    f=open("{}/etc/xdg/autostart/lxpolkit.desktop".format(get.installDIR()),"a")
    f.write("OnlyShowIn=LXDE;")
    f.close()
    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

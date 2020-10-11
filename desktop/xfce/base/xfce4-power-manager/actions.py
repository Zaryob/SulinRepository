#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --sbindir=/usr/bin \
                         --libexecdir=/usr/lib \
                         --enable-polkit \
                         --enable-dpms")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    f=open("{}/etc/xdg/autostart/xfce4-power-manager.desktop".format(get.installDIR()),"a")
    f.write("OnlyShowIn=XFCE;")
    f.close()

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")

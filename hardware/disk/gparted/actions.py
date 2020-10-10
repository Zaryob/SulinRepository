#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import get
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools

def setup():
    autotools.configure("--prefix=/usr \
      --sbindir=/usr/bin \
      --enable-online-resize \
      --enable-libparted-dmraid \
      --enable-xhost-root")

def build():
    autotools.make()

def install():
    autotools.make("install DESTDIR={}".format(get.installDIR()))
    shelltools.unlink("{}/usr/share/icons/hicolor/icon-theme.cache".format(get.installDIR()))
    shelltools.system("install -D -m0644 org.gnome.gparted.policy \
               {}/usr/share/polkit-1/actions/org.gnome.gparted.policy".format(get.installDIR()))

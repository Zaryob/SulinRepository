#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    #shelltools.makedirs("build-gtk2")
    shelltools.makedirs("build-gtk3")
    autotools.autoreconf("-fi")

    #shelltools.cd("build-gtk2")
    #shelltools.system("../configure \
    #                     --prefix=/usr \
    #                     --sysconfdir=/etc")
    #shelltools.cd("..")
    shelltools.cd("build-gtk3")
    shelltools.system("../configure \
                         --enable-dbus \
                         --prefix=/usr \
                         --sysconfdir=/etc \
                         --enable-gtk3")

def build():
    #shelltools.cd("build-gtk2")
    #autotools.make()
    #shelltools.cd("..")
    shelltools.cd("build-gtk3")
    autotools.make()

def install():
    #shelltools.cd("build-gtk2")
    #autotools.install()
    #shelltools.cd("..")
    shelltools.cd("build-gtk3")
    autotools.install()
    shelltools.cd("..")
    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

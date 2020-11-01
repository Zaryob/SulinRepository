#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

#WorkDir="libindicator-12.10.2+14.04.20140402"

def setup():

    shelltools.system("sed -i 's/-Werror//' {libindicator,tools}/Makefile.am")
    shelltools.system("autoreconf -fvi")
    autotools.configure("-prefix=/usr \
      --localstatedir=/var \
      --libexecdir=/usr/lib/libindicator \
      --sysconfdir=/etc \
      --with-gtk=3 \
      --disable-static \
      --disable-tests")
    shelltools.system("sed -i 's/-lglib-2.0-lm/-lglib-2.0 -lm/' {libindicator,tools}/Makefile")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR={}".format(get.installDIR()))

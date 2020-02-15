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
    shelltools.system("sed -i '/pager.c/d' plugins/Makefile.am")
    shelltools.system("sed -i '/STATIC_PAGER/d' src/private.h")
    shelltools.system("sed -i 's/libwnck-3.0//' configure.ac")
    autotools.autoreconf("-fi")
    shelltools.export("CFLAGS","{} -lgmodule-2.0".format(get.CFLAGS()))
    autotools.configure("--with-plugins=all \
                         --enable-man \
                         --enable-gtk3")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()
    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--with-plugins=all \
                         --enable-man \
                         --enable-gtk3")

    #sed -i '/pager.c/d' plugins/Makefile.am
    #sed -i '/STATIC_PAGER/d' src/private.h
    #sed -i 's/libwnck-3.0//' configure.ac

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()
    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

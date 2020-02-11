#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

WorkDir="grub-%s" % (get.srcVERSION().replace("_", "~"))

def setup():
    platform="pc"
    if get.buildTYPE() == "efi":
        platform="efi"
    elif get.buildTYPE() == "efi32":
        platform="efi --target=i386"
    shelltools.system('CFLAGS="" CXXFLAGS="" LDFLAGS="" ./configure --prefix=/usr  \
        --sbindir=/sbin        \
        --sysconfdir=/etc      \
        --disable-efiemu       \
        --with-platform='+platform+'    \
        --disable-werror')

def build():
    shelltools.system('CFLAGS="-fno-stack-protector" CXXFLAGS="" LDFLAGS="" make -j5')

def install():
    shelltools.system("CFLAGS="" CXXFLAGS="" LDFLAGS="" make install DESTDIR={}".format(get.installDIR()))


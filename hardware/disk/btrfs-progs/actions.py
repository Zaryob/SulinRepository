#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("PYTHON=/usr/bin/python3 --with-python --with-crypto=libgcrypt --disable-zstd")

def build():
    autotools.make("CC=%s" % get.CC())
    autotools.make("V=1 CC=%s CFLAGS=\"%s\"" % (get.CC(), get.CFLAGS()))
    autotools.make("V=1 CC=%s CFLAGS=\"%s\" btrfs-select-super" % (get.CC(), get.CFLAGS()))

def install():
    autotools.rawInstall("prefix=/usr DESTDIR=%s" % get.installDIR())
    inarytools.remove("/usr/lib/*.a")

    inarytools.dodoc("COPYING")

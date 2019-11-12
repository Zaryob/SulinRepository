#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


def setup():
    shelltootls
    shelltools.system("sed -i 's/cp -p/cp/' build/make/Makefile ")
    shelltools.makedirs("libvpx-build")
    shelltools.cd("libvpx-build")
    shelltools.system("../configure --prefix=/usr \
                       --enable-shared  \
                       --disable-static ")


def build():
    shelltools.cd("libvpx-build")
    shelltools.system("make -j1 LDFLAGS=\"{} -fPIC\"".format(get.LDFLAGS()))

def install():
    shelltools.cd("libvpx-build")
    autotools.rawInstall("DESTDIR=%s/" % get.installDIR())
    shelltools.cd("..")
    inarytools.dodoc("AUTHORS", "CHANGELOG", "LICENSE", "PATENTS")

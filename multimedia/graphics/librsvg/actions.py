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
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    if get.buildTYPE() != "emul32":
        shelltools.system("RUST_TARGET=x86_64-unknown-linux-gnu \
                          ./configure --prefix=/usr --sysconfdir=/etc \
                          --libdir=/usr/lib \
                          --enable-svgz \
                          --disable-gtk-doc")
    else:
        shelltools.system("RUST_TARGET=i686-unknown-linux-gnu \
                          ./configure --prefix=/usr --sysconfdir=/etc \
                          --libdir=/usr/lib32 \
                          --disable-vala \
                          --disable-introspection \
                          --enable-svgz --disable-gtk-doc\
                          --build=i686-pc-linux-gnu --host=i686-pc-linux-gnu")

def build():
    if get.buildTYPE() != "emul32":
        shelltools.export("RUST_TARGET","x86_64-unknown-linux-gnu")
    else:
        shelltools.export("RUST_TARGET","i686-unknown-linux-gnu")

    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

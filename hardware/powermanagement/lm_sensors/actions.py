#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def build():
    if get.buildTYPE() == "emul32":
        shelltools.system("  sed -i 's/CC := gcc/CC := gcc -m32/' Makefile")
    autotools.make("PREFIX=/usr")

def install():
    if get.buildTYPE() == "emul32":
        options="LIBDIR=/usr/lib32"
    else:
        options="LIBDIR=/usr/lib"
    autotools.rawInstall("PREFIX=/usr BUILD_STATIC_LIB=0 MANDIR=/%s PROG_EXTRA=sensord DESTDIR=%s %s user_install" % (get.manDIR(), get.installDIR(),options))

    inarytools.dodoc("CHANGES", "CONTRIBUTORS", "README")

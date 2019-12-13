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
    inarytools.dosed("Makefile", "CC = .*", "CC = %s" % get.CC())
    inarytools.dosed("Makefile", "^CFLAGS=", "CFLAGS=%s " % get.CFLAGS())

def build():
    autotools.make("BUILD_SHARED=1")

def install():
    autotools.rawInstall("PREFIX=%s/usr \
                          INSTALL_DIR=%s/sbin \
                          INSTALL_LIB=%s/usr/lib \
                          INSTALL_INC=%s/usr/include \
                          INSTALL_MAN=%s/usr/share/man" % ((get.installDIR(),)*5))

    inarytools.dodoc("COPYING", "README")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    shelltools.export("CFLAGS", "-Os")
    autotools.make('EXTRA_CFLAGS="-Os" EFIDIR="/boot/EFI"')

def install():
    inarytools.dosed("Makefile","BINDIR := /usr/sbin","BINDIR := %s/usr/sbin" % get.installDIR())

    shelltools.makedirs("%s/usr/sbin" % get.installDIR())
    #shelltools.makedirs("%s/usr/lib" % get.installDIR())
    shelltools.makedirs("%s/usr/share/man" % get.installDIR())
    shelltools.makedirs("%s/usr/include" % get.installDIR())

    autotools.rawInstall('DESTDIR=%s EFIDIR="/boot/EFI"' % get.installDIR())
    # inarytools.insinto("/usr/lib", "src/lib/*.o")
    inarytools.insinto("/usr/share/man", "src/*.8")
    inarytools.insinto("/usr/include", "src/include/*.h")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def builddiet():
    autotools.make("clean")
    shelltools.export("CC", "diet %s %s %s %s -DHAVE_STDINT_H -Os -static" % (get.CC(), get.CFLAGS(), get.CXXFLAGS(), get.LDFLAGS()))
    autotools.make("mdadm.static")
    autotools.make("mdassemble.static")

    inarytools.insinto("/sbin", "mdadm.static")
    inarytools.insinto("/sbin", "mdassemble.static")

def build():
    inarytools.dosed("Makefile", "(Wall) -Werror", "\\1")
    autotools.make("SYSCONFDIR=/%s MDASSEMBLE_AUTO=1 mdadm mdmon" % get.confDIR())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove the udev file as its shipped with udev package
    inarytools.remove("/lib/udev/rules.d/*")

    # Install config file
    inarytools.insinto("/etc", "mdadm.conf-example", "mdadm.conf")

    #builddiet()

    inarytools.dodoc("TODO", "ChangeLog", "COPYING", "mdadm.conf-example", "misc/*")

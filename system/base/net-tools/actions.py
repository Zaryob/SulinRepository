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
    inarytools.dosed("Makefile", "(?m)^(COPTS =.*)", "COPTS = %s -fPIE" % get.CFLAGS())
    inarytools.dosed("Makefile", "(?m)^(LOPTS =.*)", "LOPTS = %s -pie" % get.LDFLAGS())

def build():
    shelltools.export("CC", get.CC())

    autotools.make("libdir")
    autotools.make()
    autotools.make("ether-wake")
    autotools.make("i18ndir")

def install():
    autotools.rawInstall("BASEDIR=%s" % get.installDIR())

    inarytools.dosbin("ether-wake")
    inarytools.dosym("/bin/hostname", "/usr/bin/hostname")

    inarytools.dodoc("README", "README.ipv6", "TODO")

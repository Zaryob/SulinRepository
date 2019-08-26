#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "sysvinit-%s" % get.srcVERSION()

def build():
    autotools.make("-C src CC=\"%s\" CFLAGS=\"%s -D_GNU_SOURCE\" LCRYPT=\"-lcrypt\"" % (get.CC(), get.CFLAGS()))

def install():
    shelltools.cd("src")
    autotools.rawInstall("ROOT='%s' STRIP=/bin/true" % get.installDIR())

    inarytools.remove("/bin/pidof")
    inarytools.dosym("killall5", "/sbin/pidof")

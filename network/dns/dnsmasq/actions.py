#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Suleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    autotools.make("COPTS=\"$_build_copts\" \
                    PREFIX=/usr \
                    BINDIR=/usr/bin \
                    all-i18n")

def install():
    autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())
    inarytools.insinto("/etc/dbus-1/system.d", "dbus/dnsmasq.conf", "dnsmasq.conf")

    inarytools.dodir("/var/lib/dnsmasq")

    inarytools.dodoc("CHANGELOG", "COPYING", "COPYING-v3", "FAQ")
    inarytools.dohtml("doc.html", "setup.html")

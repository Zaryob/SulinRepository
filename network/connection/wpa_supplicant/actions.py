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
    shelltools.cd("wpa_supplicant")

    #Enable syslog output
    cflags = get.CFLAGS() + " -DCONFIG_DEBUG_SYSLOG"
    shelltools.export("CFLAGS", cflags)

    autotools.make("V=1")
    autotools.make("eapol_test")

def install():
    shelltools.cd("wpa_supplicant")

    for bin in ["wpa_supplicant", "wpa_cli", "wpa_passphrase", "eapol_test"]:
        inarytools.dosbin(bin)

    # Install dbus files
    inarytools.insinto("/usr/share/dbus-1/system-services", "dbus/*.service")
    inarytools.insinto("/etc/dbus-1/system.d", "dbus/dbus-wpa_supplicant.conf", "wpa_supplicant.conf")

    inarytools.doman("doc/docbook/*.5")
    inarytools.doman("doc/docbook/*.8")
    inarytools.newdoc("wpa_supplicant.conf", "wpa_supplicant.conf.example")

    inarytools.dodoc("ChangeLog", "../COPYING", "eap_testing.txt", "../README", "todo.txt")
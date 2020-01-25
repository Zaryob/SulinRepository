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
    shelltools.export("CXXFLAGS","")
    shelltools.export("CFLAGS","")
    shelltools.export("LDFLAGS","")
    shelltools.export("PYTHON", "/usr/bin/python3")

    autotools.make("LIBDIR=/usr/lib BINDIR=/usr/bin")
    autotools.make("LIBDIR=/usr/lib BINDIR=/usr/bin eapol_test")

def install():
    shelltools.cd("wpa_supplicant")
    autotools.rawInstall('LIBDIR="/usr/lib" BINDIR="/usr/bin" DESTDIR={}'.format(get.installDIR()))
    shelltools.system('install -Dm755 "eapol_test" "{}/usr/bin/eapol_test"'.format(get.installDIR()))
    #dbus
    shelltools.system('install -Dm644 "dbus/fi.w1.wpa_supplicant1.service" "{}/usr/share/dbus-1/system-services/fi.w1.wpa_supplicant1.service"'.format(get.installDIR()))
    shelltools.system('install -Dm644 "dbus/dbus-wpa_supplicant.conf" "{}/etc/dbus-1/system.d/wpa_supplicant.conf"'.format(get.installDIR()))
    shelltools.system('install -d {}/etc/dbus-1/system.d'.format(get.installDIR()))
    shelltools.system('install -d {}/var/run/wpa_supplicant'.format(get.installDIR()))
	
	  
	  

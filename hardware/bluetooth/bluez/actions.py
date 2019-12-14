#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():

    #shelltools.system("sed -i -e '/SystemdService/d' obexd/src/org.bluez.obex.service")
    inarytools.dosed("obexd/src/org.bluez.obex.service", "SystemdService", deleteLine=True)
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --libexecdir=/usr/libexec/ \
                         --enable-sixaxis \
                         --enable-experimental \
                         --disable-android \
                         --enable-datafiles \
                         --enable-optimization \
                         --enable-pie \
                         --enable-threads \
                         --enable-library \
                         --enable-tools \
                         --enable-manpages \
                         --enable-monitor \
                         --enable-udev \
                         --enable-test \
                         --disable-systemd")


    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install-pkglibexecPROGRAMS install-dbussessionbusDATA install-dbussystembusDATA install-dbusDATA install-man8" % get.installDIR())


    # Install conf files
    for i in ["profiles/input", "profiles/network" ,"src"]:
        inarytools.insinto("/etc/bluetooth", "%s/*.conf" % (i))


    # Simple test tools
    for i in [  "agent.py",
                "list-devices",
                "test-adapter",
                "test-manager",
                "bluezutils.py",
                "map-client",
                "test-device",
                "test-mesh",
                "dbusdef.py",
                "monitor-bluetooth",
                "test-discovery",
                "test-nap",
                "opp-client",
                "test-gatt-profile",
                "test-network",
                "example-gatt-client",
                "pbap-client",
                "simple-agent",
                "test-health",
                "test-profile",
                "example-gatt-server",
                "sap_client.py",
                "simple-endpoint",
                "test-health-sink",
                "test-sap-server",
                "ftp-client",
                "simple-player",
                "test-hfp"]:
        inarytools.dobin("test/%s" % i)
   # for i in
      #  inarytools.dodoc("doc/%s" % i)
    # Install documents
    inarytools.dodoc("AUTHORS", "ChangeLog", "README")

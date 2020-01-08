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
    autotools.rawConfigure("--prefix=/usr \
                            --sbindir=/usr/bin \
                            --sysconfdir=/etc \
                            --enable-binary-leases \
                            --with-srv-lease-file=/var/lib/dhcpd/dhcpd.leases \
                            --with-srv6-lease-file=/var/lib/dhcpd/dhcpd6.leases \
                            --with-cli-lease-file=/var/lib/dhclient/dhclient.leases \
                            --with-cli6-lease-file=/var/lib/dhclient/dhclient6.leases \
                            --with-srv-pid-file=/run/dhcpd.pid \
                            --with-srv6-pid-file=/run/dhcpd6.pid \
                            --with-cli-pid-file=/run/dhclient.pid \
                            --with-cli6-pid-file=/run/dhclient6.pid \
                            --with-relay-pid-file=/run/dhcrelay.pid \
                            --with-ldap \
                            --with-ldapcrypto")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove files we don't want
    inarytools.remove("/etc/dhcpd.conf.example")
    inarytools.remove("/etc/dhclient.conf.example")

    # Install dhcp.schema for LDAP configuration
    inarytools.insinto("/etc/openldap/schema", "contrib/ldap/dhcp.schema")

    # Create directory hierarchy in /var
    inarytools.dodir("/var/lib/dhcpd")
    inarytools.dodir("/var/lib/dhclient")

    # Sample configuration files
    inarytools.insinto("/usr/share/doc/dhcp", "client/dhclient.conf.5", "dhclient.conf.exsample")
    inarytools.insinto("/usr/share/doc/dhcp", "server/dhcpd.conf.5", "dhcpd.conf.example")
    inarytools.insinto("/usr/share/doc/dhcp", "doc/examples/dhclient-dhcpv6.conf")
    inarytools.insinto("/usr/share/doc/dhcp", "doc/examples/dhcpd-dhcpv6.conf")

    inarytools.dodoc("LICENSE", "README", "RELNOTES")

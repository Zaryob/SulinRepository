#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import pythonmodules
from inary.actionsapi import perlmodules
from inary.actionsapi import shelltools
from inary.actionsapi import get

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

MIBS = "host agentx smux \
       ucd-snmp/diskio tcp-mib udp-mib mibII/mta_sendmail \
       ip-mib/ipv4InterfaceTable ip-mib/ipv6InterfaceTable \
       ip-mib/ipAddressPrefixTable/ipAddressPrefixTable \
       ip-mib/ipDefaultRouterTable/ipDefaultRouterTable \
       ip-mib/ipv6ScopeZoneIndexTable ip-mib/ipIfStatsTable \
       sctp-mib rmon-mib etherlike-mib"

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure('PYTHON=/usr/bin/python \
                         --enable-shared \
                         --disable-static \
                         --without-rpm \
                         --with-sys-location=Unknown \
                         --with-sys-contact=root@Unknown \
                         --with-default-snmp-version=3 \
                         --with-logfile=/var/log/snmpd.log \
                         --with-persistent-directory=/var/lib/net-snmp \
                         --with-mib-modules="%s" \
                         --enable-ipv6 \
                         --enable-ucd-snmp-compatibility \
                         --with-openssl \
                         --with-pic \
                         --enable-embedded-perl \
                         --with-libwrap \
                         --enable-as-needed \
                         --without-root-access \
                         --enable-mfd-rewrites \
                         --with-temp-file-pattern="/run/net-snmp/snmp-tmp-XXXXXX" \
                         --enable-local-smux' % MIBS)

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-j1")

    shelltools.cd("python")
    pythonmodules.compile("--basedir=..", pyVer="2")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("python")
    pythonmodules.install('--skip-build --basedir=..', pyVer="2")
    shelltools.cd("..")

    inarytools.insinto("/etc/snmp/", "EXAMPLE.conf", "snmpd.conf.example")

    inarytools.dodir("/var/lib/net-snmp")
    inarytools.dodir("/etc/snmp")

    inarytools.dodoc("AGENT.txt", "ChangeLog", "FAQ", "NEWS", "PORTING", "README", "TODO")

    perlmodules.removePacklist()
    perlmodules.removePodfiles()

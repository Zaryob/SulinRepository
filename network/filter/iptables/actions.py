#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import libtools
from inary.actionsapi import get

def setup():

    autotools.autoreconf("-vif")
    libtools.libtoolize()
    autotools.configure("--sbindir=/sbin \
                         --libexecdir=/usr/lib \
                         --without-kernel \
                         --enable-devel \
                         --disable-nftables \
                         --enable-libipq \
                         --enable-shared \
                         --enable-static")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("V=1")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    inarytools.insinto("/usr/include", "include/iptables.h")
    inarytools.insinto("/usr/include", "include/ip6tables.h")
    inarytools.insinto("/usr/include/libiptc", "include/libiptc/*.h")

    inarytools.dodir("/var/lib/iptables")
    inarytools.dodir("/etc/iptables")

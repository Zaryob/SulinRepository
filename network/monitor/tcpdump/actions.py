#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Suleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -O2 -DIP_MAX_MEMBERSHIPS=20" % get.CFLAGS())

    autotools.autoreconf("-vfi")
    autotools.configure("--enable-ipv6 \
                         --with-ssl \
                         --with-smi \
                         --enable-ipv6 \
                         --disable-smb \
                         --mandir=/usr/share/man")

def build():
    autotools.make()

def install():
    inarytools.dosbin("tcpdump")
    inarytools.doman("tcpdump.1")
    inarytools.dodoc("CHANGES", "LICENSE", "README", "CREDITS", "PLATFORMS", "VERSION", "*.awk")

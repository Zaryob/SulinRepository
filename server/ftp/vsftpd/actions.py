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

def build():
    autotools.make('CC="%s" CFLAGS="%s -fpie" LINK="-pie -lssl" LDFLAGS="%s"' % (get.CC(),get.CFLAGS(),get.LDFLAGS()))

def install():
    inarytools.dosbin("vsftpd")

    inarytools.dodir("/data/user/ftp")
    inarytools.dodir("/data/user/ftp/incoming")
    inarytools.dodir("/usr/share/vsftpd/empty")
    inarytools.dodir("/var/log/vsftpd")

    inarytools.newdoc("vsftpd.conf", "vsftpd.conf.example")
    inarytools.doman("vsftpd.conf.5", "vsftpd.8")
    inarytools.insinto("/usr/share/doc/%s" % get.srcNAME(), "SECURITY")
    inarytools.insinto("/usr/share/doc/%s" % get.srcNAME(), "EXAMPLE")
    inarytools.dodoc("AUDIT", "BENCHMARKS", "BUGS", "Changelog", "FAQ",\
                    "LICENSE", "README*", "REFS", "REWARD", "SIZE", \
                    "SPEED", "TODO", "TUNING")

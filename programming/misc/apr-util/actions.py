#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

# to avoid sandbox violations during make test
shelltools.export("ODBCINI", get.workDIR())
shelltools.export("ODBCSYSINI", get.workDIR())

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--with-apr=/usr \
                         --includedir=/usr/include/apr-1 \
                         --with-ldap \
                         --without-gdbm \
                         --with-sqlite3 \
                         --with-pgsql \
                         --with-odbc=/usr/bin/odbc_config \
                         --with-mysql \
                         --without-freetds \
                         --with-berkeley-db \
                         --without-sqlite2")
    
    #inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def check():
    autotools.make("-j1 test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dosed("%s/usr/bin/apu-1-config" % get.installDIR(), get.workDIR(), "")

    inarytools.dodoc("CHANGES", "NOTICE")

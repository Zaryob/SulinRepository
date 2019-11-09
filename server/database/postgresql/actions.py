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
    autotools.configure("PYTHON=/usr/bin/python3 \
                         --with-python \
                         --with-perl \
                         --include=/usr/include/postgresql \
                         --with-includes=/usr/include/libxml2/ \
                         --with-tcl \
                         --with-krb5 \
                         --with-openssl \
                         --enable-nls \
                         --with-pam \
                         --with-libxml \
                         --with-libxslt \
                         --with-ldap \
                         --enable-integer-datetimes \
                         --enable-thread-safety \
                         --enable-depend \
                         --host=%s \
                         --libdir=/usr/lib \
                         --disable-rpath \
                         --with-docdir=/usr/share/doc/postgresql" % get.CHOST())

def build():
    if get.LDFLAGS():
        ld = "-j1 LD=%s %s" % (get.LD(), get.LDFLAGS())
    else:
        ld = "-j1 LD=%s" % get.LD()

    autotools.make(ld)

    shelltools.cd("contrib")
    autotools.make(ld)
    shelltools.cd("..")

    shelltools.cd("contrib/xml2")
    autotools.make(ld)
    shelltools.cd("../..")

    shelltools.cd("src/interfaces/libpq")
    autotools.make(ld)
    shelltools.cd("../../..")

    shelltools.cd("doc")
    autotools.make(ld)
    shelltools.cd("..")

def install():
    autotools.rawInstall("DESTDIR=%s LIBDIR=%s/usr/lib" % (get.installDIR(), get.installDIR()))

    shelltools.cd("contrib")
    autotools.rawInstall("DESTDIR=%s LIBDIR=%s/usr/lib" % (get.installDIR(), get.installDIR()))
    shelltools.cd("..")

    shelltools.cd("contrib/xml2")
    autotools.rawInstall("DESTDIR=%s LIBDIR=%s/usr/lib" % (get.installDIR(), get.installDIR()))
    shelltools.cd("../..")

    shelltools.cd("src/interfaces/libpq")
    autotools.rawInstall("DESTDIR=%s LIBDIR=%s/usr/lib" % (get.installDIR(), get.installDIR()))
    shelltools.cd("../../..")

    shelltools.cd("doc")
    autotools.rawInstall("DESTDIR=%s LIBDIR=%s/usr/lib" % (get.installDIR(), get.installDIR()))
    shelltools.cd("..")

    # No static libs
    inarytools.remove("/usr/lib/*.a")

    inarytools.dodoc("README", "HISTORY", "COPYRIGHT")
    inarytools.dodoc("doc/MISSING_FEATURES", "doc/KNOWN_BUGS", "doc/TODO")
    inarytools.dodir("/var/lib/postgresql")
    inarytools.dodir("/var/lib/postgresql/data")
    inarytools.dodir("/var/lib/postgresql/backups")

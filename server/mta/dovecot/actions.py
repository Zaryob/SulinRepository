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

WorkDIR="dovecot-2.3.10"

def setup():
    inarytools.dosed("doc/mkcert.sh", "dovecot-openssl.cnf", "/etc/dovecot/ssl/openssl.cnf")
    autotools.configure("--sysconfdir=/etc/dovecot \
                         --localstatedir=/var \
                            --with-nss \
                            --with-pam \
                            --with-mysql \
                            --with-pgsql \
                            --with-sqlite \
                            --with-ssl=openssl \
                            --with-ssldir=/etc/ssl \
                            --with-gssapi \
                            --with-ldap=plugin \
                            --with-lua=plugin \
                            --with-zlib \
                            --with-bzlib \
                            --with-lzma \
                            --with-lz4 \
                            --with-libcap \
                            --with-solr \
                            --with-lucene \
                            --with-docs \
                            --disable-static")
    autotools.make("dovecot-config")

    shelltools.cd("../dovecot-2.3-pigeonhole-0.5.10/")
    autotools.configure("--with-dovecot=../dovecot-2.3.10/ \
                        --with-moduledir=/usr/lib/dovecot/modules \
                        --disable-static")

def build():
    autotools.make()
    shelltools.cd("../dovecot-2.3-pigeonhole-0.5.10/")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../dovecot-2.3-pigeonhole-0.5.10/")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../dovecot-2.3.10/")


    inarytools.insinto("/usr/lib/dovecot/mkcert.sh", "doc/mkcert.sh")
    inarytools.insinto("/etc/dovecot/", "doc/example-config/*.conf")
    inarytools.insinto("/etc/dovecot/", "doc/example-config/*.ext")
    inarytools.insinto("/etc/dovecot/conf.d", "doc/example-config/conf.d/*.conf")
    inarytools.insinto("/etc/dovecot/conf.d", "doc/example-config/conf.d/*.ext")

    inarytools.dodoc("AUTHORS", "NEWS", "README", "TODO")
    inarytools.dodoc("doc/*.txt", "doc/*.cnf")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    autotools.autoreconf("-vfi --no-recursive -I config ")

    inarytools.cflags.add("-fPIC")

    # Don't disable ldap support to break circular dep. with openldap
    # As workaround, we remove openldap-client runtime dep. in pspec
    autotools.configure("--with-saslauthd=/run/saslauthd \
                         --with-pwcheck=/var/lib/sasl2 \
                         --with-configdir=/etc/sasl2 \
                         --with-plugindir=/usr/lib/sasl2 \
                         --with-dbpath=/etc/sasl2/sasldb2 \
                         --with-pam \
                         --without-ldap \
                         --with-openssl \
                         --with-dblib=gdbm \
                         --with-gss_impl=mit \
                         --with-devrandom=/dev/urandom \
                         --without-pgsql \
                         --without-mysql \
                         --enable-anon \
                         --enable-cram \
                         --enable-digest \
                         --enable-gssapi \
                         --enable-login \
                         --enable-ntlm \
                         --enable-plain \
                         --disable-ldapdb \
                         --enable-checkapop \
                         --enable-alwaystrue \
                         --disable-java \
                         --disable-krb4 \
                         --disable-otp \
                         --disable-srp \
                         --disable-sql \
                         --disable-passdss \
                         --disable-macos-framework \
                         --disable-static")

    # for remove unused
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-j1")
    autotools.make("-C saslauthd testsaslauthd")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s -C plugins" % get.installDIR())

    inarytools.dodir("/etc/sasl2")
    inarytools.dodir("/run/saslauthd")

    inarytools.dohtml("doc/html/*")
    inarytools.dodoc("AUTHORS", "COPYING", "ChangeLog")

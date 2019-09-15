#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

KeepSpecial = ["libtool"]

def setup():
    inarytools.dosed(
        "include/ldap_defaults.h",
        "(#define LDAPI_SOCK).*",
        '\\1 "/run/openldap/slapd.sock"'
    )
    inarytools.dosed("servers/slapd/Makefile.in", "(\$\(DESTDIR\))\$\(localstatedir\)(\/run)", r"\1\2")

    inarytools.flags.add("-D_REENTRANT -D_GNU_SOURCE -fPIC -Wl,--as-needed -DLDAP_CONNECTIONLESS")
    #inarytools.ldflags.add("-pie")

    options = "--prefix=/usr \
               --disable-bdb \
               --disable-hdb \
               --enable-sql \
               --enable-backends=mod \
               --enable-slapd \
               --enable-passwd=mod \
               --enable-dnssrv=mod \
               --enable-ldap \
               --enable-wrappers \
               --enable-meta=mod \
               --enable-monitor=mod \
               --enable-null=mod \
               --enable-shell=mod \
               --enable-rewrite \
               --enable-rlookups \
               --enable-aci \
               --enable-modules \
               --enable-cleartext \
               --enable-lmpasswd \
               --enable-spasswd \
               --enable-slapi \
               --enable-dyngroup \
               --enable-proxycache \
               --enable-perl \
               --enable-syslog \
               --enable-dynamic \
               --enable-local \
               --enable-proctitle \
               --enable-overlays=mod \
               --enable-ndb=no \
               --with-pic \
               --with-threads \
               --with-cyrus-sasl \
               --without-fetch \
               --without-threads \
               --enable-crypt \
               --enable-ipv6 \
               --enable-dynacl \
               --enable-shared \
               --disable-static \
               --disable-slp \
               --localstatedir=/var/lib"

    if get.buildTYPE() == "emul32":
        options =  " --prefix=/emul32 \
                     --libdir=/usr/lib32 \
                     --libexecdir=/emul32/libexec \
                     --disable-bdb \
                     --disable-hdb \
                     --disable-wrappers \
                     --disable-spasswd \
                     --disable-perl \
                     --without-tls \
                     --without-cyrus-sasl"
    else: options += " --with-tls=auto"

    shelltools.export("AUTOMAKE", "/bin/true")
    autotools.autoreconf("-fi")
    autotools.configure(options)

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        return

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


    inarytools.dodir("/run/openldap")
    inarytools.dodir("/etc/openldap/ssl")

    inarytools.dodoc("ANNOUNCEMENT", "CHANGES", "COPYRIGHT", "README", "LICENSE")

    inarytools.remove("/usr/lib/*.la")
    inarytools.remove("/usr/libexec/openldap/*.la")

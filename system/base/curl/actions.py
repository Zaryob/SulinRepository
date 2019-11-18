#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --enable-dependency-tracking \
                         --disable-ldap \
                         --disable-ldaps \
                         --with-ssl \
                         --with-zlib \
                         --with-libidn \
                         --with-libssh2 \
                         --with-openssl \
                         --with-gssapi=no \
                         --with-nghttp2 \
                         --with-libmetalink \
                         --without-librtmp \
                         --enable-ipv6 \
                         --enable-http \
                         --enable-ftp \
                         --enable-file \
                         --enable-dict \
                         --enable-manual \
                         --enable-gopher \
                         --enable-telnet \
                         --enable-largefile \
                         --enable-nonblocking \
                         --enable-threaded-resolver \
                         --enable-hidden-symbols \
                         --disable-versioned-symbols \
                         ac_cv_header_gss_h=no \
                         --with-ca-bundle=/etc/ssl/certs/ca-certificates.crt \
                         --prefix=/usr \
                         --with-random=/dev/urandom \
                         --mandir=/usr/share/man ")


def build():
    autotools.make()

def check():
    #shelltools.export("LD_LIBRARY_PATH", "%s/lib" % get.curDIR())
    #autotools.make("-C tests test")
    pass

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("CHANGES", "docs/*.md")

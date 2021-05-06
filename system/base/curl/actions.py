#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
import os
env=os.environ.copy()
from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    if get.buildTYPE() == "emul32":
        set_emul32()
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
                         --without-zstd \
                         --without-brotli \
                         --with-nghttp2 \
                         --with-ngtcp2\
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
    if get.buildTYPE() == "emul32":
        set_emul32()
        shelltools.system("make -j$(nproc)")
        return
    autotools.make()

def set_emul32():
    os.environ.clear()
    os.environ.update(env)
    shelltools.export("CC", "gcc -m32")
    shelltools.export("CXX", "g++ -m32")
    shelltools.export("HOST", "x86_64")
    shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

def check():
    pass
    #shelltools.export("LD_LIBRARY_PATH", "%s/lib" % get.curDIR())
    #autotools.make("-C tests test")

def install():
    
    if get.buildTYPE() == "emul32":
        shelltools.system("make install DESTDIR=%s/emul32" % get.installDIR())
        shelltools.copytree("%s/emul32/usr/lib32" % get.installDIR(), "%s/usr/lib32" % get.installDIR())
        inarytools.removeDir("/emul32")
        return
    shelltools.system("make install DESTDIR=%s/" % get.installDIR())
    inarytools.dodoc("CHANGES", "docs/*.md")

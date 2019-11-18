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
    shelltools.system("./buildconf")
    shelltools.export("ac_cv_search_shm_open", "no")

    autotools.configure("--disable-static \
                         --includedir=/usr/include/apr-1 \
                         --with-installbuilddir=/usr/lib/apr-1/build \
                         --with-devrandom=/dev/urandom \
                         --enable-nonportable-atomics --without-sendfile")

    # Make it use system's libtool
    inarytools.dosed("build/apr_rules.mk", "\$\(apr_builddir\)\/libtool", "/usr/bin/libtool")
    inarytools.dosed("apr-1-config", "\$\{installbuilddir\}\/libtool", "/usr/bin/libtool")

    # fix unused-direct-shlib-dependency
    inarytools.dosed("libtool", "( -shared )", " -Wl,-O1,--as-needed\\1")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Trim exported dependencies
    inarytools.dosed("%s/usr/lib/pkgconfig/*.pc" % get.installDIR(), "-luuid -lcrypt", "")
    inarytools.dosed("%s/usr/bin/apr-1-config" % get.installDIR(), "-luuid -lcrypt", "")

    # Install find_apr.m4
    inarytools.dodir("/usr/share/aclocal")
    inarytools.insinto("/usr/share/aclocal", "build/find_apr.m4")

    inarytools.dodoc("CHANGES", "LICENSE", "NOTICE")

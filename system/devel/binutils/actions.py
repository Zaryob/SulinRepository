#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

# linker = "gold"
linker = "ld"
multilib = "--enable-multilib" if get.ARCH() == "x86_64" else ""


def setup():
    shelltools.system('sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" libiberty/configure')

    autotools.configure('--enable-shared \
                         --build=x86_64-pc-linux-gnu \
                         --enable-threads \
                         --enable-ld=default \
                         --enable-gold \
                         --enable-plugins \
                         --with-pkgversion="Sulin" \
                         --with-bugurl=http://gitlab.com/sulinos/main/issues \
                         %s \
                         --with-pic \
                         --disable-nls \
                         --disable-werror' % ( multilib))

def build():
    autotools.make("configure-host")
    autotools.make()

def check():
    autotools.make("check -j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.make("-C libiberty clean")
    autotools.make('CFLAGS="-fPIC %s" -C libiberty' % get.CFLAGS())

    autotools.make("-C bfd clean")
    autotools.make('CFLAGS="-fPIC %s" -C bfd' % get.CFLAGS())

    inarytools.insinto("/usr/lib", "bfd/libbfd.a")
    inarytools.insinto("/usr/lib", "libiberty/libiberty.a")
    inarytools.insinto("/usr/include", "include/libiberty.h")
    inarytools.insinto("/usr/include", "include/demangle.h")

    # Copy plugin-api.h file to build LLVM with LLVM gold plugin
    inarytools.insinto("/usr/include", "include/plugin-api.h")
    #inarytools.remove("/usr/share/info/configure.info")
    #inarytools.remove("/usr/share/info/standards.info")

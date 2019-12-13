#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

import os

verMajor = get.srcVERSION()

arch = get.ARCH().replace("x86_64", "x86-64")

opt_unwind = "--with-system-libunwind" if get.ARCH() == "x86_64" else "--without-system-libunwind"
opt_arch = "--with-arch_32=i686" if get.ARCH() == "x86_64" else "--with-arch=i686"
opt_multilib = "--enable-multilib --with-multilib-list=m32,m64" if get.ARCH() == "x86_64" else ""

# WARNING: even -fomit-frame-pointer may break the build, stack protector, fortify source etc. are off limits
cflags = "-O2 -g"


def removeSulinLinuxSection(_dir):
    for root, dirs, files in os.walk(_dir):
        for name in files:
            # FIXME: should we do this only on nonshared or all ?
            # if ("crt" in name and name.endswith(".o")) or name.endswith("nonshared.a"):
            if ("crt" in name and name.endswith(".o")) or name.endswith(".a"):
                i = os.path.join(root, name)
                shelltools.system('objcopy -R ".comment.SULIN.OPTs" -R ".note.gnu.build-id" %s' % i)

def exportFlags():
    # we set real flags with new configure settings, these are just safe optimizations
    shelltools.export("CFLAGS", cflags)
    shelltools.export("CXXFLAGS", cflags)
    # shelltools.export("LDFLAGS", "")

    # FIXME: this may not be necessary for biarch
    shelltools.export("CC", "gcc")
    shelltools.export("CXX", "g++")
    shelltools.export("LC_ALL", "en_US.UTF-8")

def setup():
    exportFlags()
    # Maintainer mode off, do not force recreation of generated files
    #shelltools.system("contrib/gcc_update --touch")
    inarytools.dosed("gcc/Makefile.in", "\.\/fixinc\.sh", "-c true")
    inarytools.dosed("gcc/configure", "^(ac_cpp='\$CPP\s\$CPPFLAGS)", r"\1 -O2")
    inarytools.dosed("libiberty/configure", "^(ac_cpp='\$CPP\s\$CPPFLAGS)", r"\1 -O2")

    shelltools.cd("../")
    shelltools.makedirs("build")
    shelltools.cd("build")

    shelltools.system('.././gcc-%s/configure \
                       --prefix=/usr \
                       --bindir=/usr/bin \
                       --libdir=/usr/lib \
                       --libexecdir=/usr/lib \
                       --includedir=/usr/include \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --with-bugurl=http://gitlab.com/sulinos/main/issues \
                       --enable-languages=c,c++,go,fortran,lto,objc,obj-c++ \
                       --enable-shared \
                       --enable-threads=posix \
                       --with-system-zlib \
                       --enable-__cxa_atexit \
                       --disable-libunwind-exceptions \
                       --enable-clocale=gnu \
                       --disable-libstdcxx-pch \
                       --disable-libssp \
                       --enable-gnu-unique-object \
                       --enable-linker-build-id \
                       --enable-lto \
                       --enable-install-libiberty \
                       --enable-gnu-indirect-function \
                       --with-linker-hash-style=gnu \
                       --enable-plugin \
                       --with-pkgversion="Sulin" \
                       --disable-werror \
                       --enable-checking=release \
                       --enable-default-pie \
                       --enable-default-ssp \
                       --enable-cet=auto \
                       --build=x86_64-pc-linux-gnu \
                       --target=x86_64-pc-linux-gnu \
                       --host=x86_64-pc-linux-gnu \
                               %s \
                               %s \
                               %s  ' % ( verMajor, opt_unwind, opt_arch, opt_multilib))

def build():
    exportFlags()

    shelltools.cd("../build")
    autotools.make('BOOT_CFLAGS="%s" bootstrap' % cflags)

def install():
    shelltools.cd("../build")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #autotools.install()

    for header in ["limits.h","syslimits.h"]:
        inarytools.insinto("/usr/lib/gcc/%s/%s/include" % (get.HOST(), verMajor) , "gcc/include-fixed/%s" % header)

    # Not needed
    inarytools.removeDir("/usr/lib/gcc/*/*/include-fixed")
    inarytools.removeDir("/usr/lib/gcc/*/*/install-tools")

    # This one comes with binutils
    inarytools.remove("/usr/lib*/libiberty.a")

    # cc symlink
    inarytools.dosym("/usr/bin/gcc" , "/usr/bin/cc")

    # /lib/cpp symlink for legacy X11 stuff
    inarytools.dosym("/usr/bin/cpp", "/lib/cpp")

    inarytools.dosym("/usr/bin/x86_64-pc-linux-gnu-gcc-ar", "/usr/bin/x86_64-pc-linux-gnu-ar")

    # Remove our options section from crt stuff
    removeSulinLinuxSection("%s/usr/lib/" % get.installDIR())
    if get.ARCH() == "x86_64":
        removeSulinLinuxSection("%s/usr/lib32/" % get.installDIR())


    # autoload gdb pretty printers
    gdbpy_dir = "/usr/share/gdb/auto-load/usr/lib/"
    inarytools.dodir(gdbpy_dir)

    gdbpy_files = shelltools.ls("%s/usr/lib/libstdc++*gdb.py*" % get.installDIR())
    for i in gdbpy_files:
        inarytools.domove("/usr/lib/%s" % shelltools.baseName(i), gdbpy_dir)

    if arch == "x86-64":
        inarytools.remove("/usr/lib32/libstdc++*gdb.py*")
    inarytools.rename("/usr/bin/go", "go1.12.2")
    inarytools.rename("/usr/bin/gofmt", "gofmt1.12.2")

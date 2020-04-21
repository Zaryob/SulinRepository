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


arch = "x86-64" if get.ARCH() == "x86_64" and not get.buildTYPE() == "emul32" else "i686"
defaultflags = "-Os -g -mno-tls-direct-seg-refs -mtune=generic -march=%s" % arch
if get.buildTYPE() == "emul32": defaultflags += " -m32 -fasynchronous-unwind-tables"
# this is getting ridiculous, also gdb3 breaks resulting binary
sysflags = "-mtune=generic -march=x86-64" if get.ARCH() == "x86_64" else "-mtune=generic -march=i686"

ldconf32bit = """/lib32
/usr/lib32
"""

def setup():
    shelltools.export("LANGUAGE","C")
    shelltools.export("LANG","C")
    shelltools.export("LC_ALL","C")

    shelltools.export("CC", "gcc %s " % defaultflags)
    shelltools.export("CXX", "g++ %s " % defaultflags)

    shelltools.export("CFLAGS", defaultflags)
    shelltools.export("CXXFLAGS", defaultflags)

    shelltools.makedirs("build")
    shelltools.cd("build")
    options = "--prefix=/usr \
               --libdir=/usr/lib \
               --mandir=/usr/share/man \
               --infodir=/usr/share/info \
               --libexecdir=/usr/lib/misc \
               --with-bugurl=http://gitlab.com/sulinos/main/issues \
               --enable-add-ons \
               --enable-bind-now \
               --enable-lock-elision \
               --enable-multi-arch \
               --enable-static-pie\
               --enable-stack-protector=all \
               --enable-kernel=4.19.217 \
               --with-headers=/usr/include \
               --enable-stackguard-randomization \
               --disable-werror"
    if get.buildTYPE() == "emul32":
        options += "\
                    --libdir=/usr/lib32 \
                    --enable-multi-arch i686-pc-linux-gnu \
                   "

    shelltools.system("../configure %s" % options)

def build():
    shelltools.cd("build")
    if get.buildTYPE() == "emul32":
        shelltools.echo("configparms","build-programs=no")
        shelltools.echo("configparms", "slibdir=/lib32")
        shelltools.echo("configparms", "rtlddir=/lib32")
        shelltools.echo("configparms", "bindir=/tmp32")
        shelltools.echo("configparms", "sbindir=/tmp32")
        shelltools.echo("configparms", "rootsbindir=/tmp32")
        shelltools.echo("configparms", "datarootdir=/tmp32/share")

        autotools.make()

        inarytools.dosed("configparms", "=no", "=yes")

    else:
        shelltools.echo("configparms", "slibdir=/lib")
        shelltools.echo("configparms", "rtlddir=/lib")

    autotools.make()


def install():
    shelltools.cd("build")

    autotools.rawInstall("install_root=%s" % get.installDIR())

    inarytools.dodir("/etc/ld.so.conf.d")

    if get.buildTYPE() != "emul32":
        #Install locales once.
        autotools.rawInstall("install_root=%s localedata/install-locales" % get.installDIR())



    if get.buildTYPE() == "emul32":
        inarytools.dosym("/lib32/ld-linux.so.2", "/lib/ld-linux.so.2")

        shelltools.echo("%s/etc/ld.so.conf.d/60-glibc-32bit.conf" % get.installDIR(), ldconf32bit)

        inarytools.removeDir("/tmp32")


    # We'll take care of the cache ourselves
    if shelltools.isFile("%s/etc/ld.so.cache" % get.installDIR()):
        inarytools.remove("/etc/ld.so.cache")

    # Prevent overwriting of the /etc/localtime symlink
    if shelltools.isFile("%s/etc/localtime" % get.installDIR()):
        inarytools.remove("/etc/localtime")

    # Nscd needs this to work
    inarytools.dodir("/var/run/nscd")
    inarytools.dodir("/var/db/nscd")

    # remove zoneinfo files since they are coming from timezone packages
    # we disable timezone build with a patch, keeping these lines for easier maintenance
    if shelltools.isDirectory("%s/usr/share/zoneinfo" % get.installDIR()):
        inarytools.removeDir("/usr/share/zoneinfo")

    #while bootstrapping whole system zic should not be removed. timezone package does not build without it. # 2013
    #for i in ["zdump","zic"]:
        #if shelltools.isFile("%s/usr/sbin/%s" % (get.installDIR(), i)):
            #inarytools.remove("/usr/sbin/%s" % i)

    shelltools.cd("..")
    inarytools.dodoc("ChangeLog", "NEWS", "README*", "LICENSES")


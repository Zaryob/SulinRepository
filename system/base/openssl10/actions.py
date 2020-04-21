#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():

    options = " --prefix=/usr \
                --libdir=lib \
                --openssldir=/etc/ssl \
                shared -Wa,--noexecstack \
                zlib enable-camellia enable-idea \
                enable-seed enable-rfc3779 enable-rc5 \
                enable-cms enable-md2 enable-mdc2 threads"
    shelltools.system("echo "+get.buildTYPE())
    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 --libdir=lib32".format(get.installDIR())
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.system("./Configure linux-elf %s" % options)
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")

    else:
        options += " enable-ec_nistp_64_gcc_128"
        shelltools.system("./Configure linux-x86_64 %s" % options)
        inarytools.dosed("Makefile", "^(SHARED_LDFLAGS=).*", "\\1 ${LDFLAGS}")
        inarytools.dosed("Makefile", "^(CFLAG=.*)", "\\1 ${CFLAGS}")

def build():
    autotools.make("depend")
    autotools.make()
    #autotools.make("rehash")

#def check():
    #Revert ca-dir patch not to fail test
    #shelltools.system("patch -p1 -R < openssl-1.0.0-beta4-ca-dir.patch")

#    homeDir = "%s/test-home" % get.workDIR()
#    shelltools.export("HOME", homeDir)
#    shelltools.makedirs(homeDir)
#    autotools.make("-j1 test")

    #Passed. So, re-patch
    #shelltools.system("patch -p1 < openssl-1.0.0-beta4-ca-dir.patch")

def install():
    if get.buildTYPE()=="emul32":
        shelltools.system("mkdir -p {}/usr/lib32".format(get.installDIR()))
        shelltools.system("install libssl.so.1.0.0 {}/usr/lib32/libssl.so.1.0.0".format(get.installDIR()))
        shelltools.system("install libcrypto.so.1.0.0 {}/usr/lib32/libcrypto.so.1.0.0".format(get.installDIR()))
    else:
        shelltools.system("mkdir -p {}/usr/lib/".format(get.installDIR()))
        shelltools.system("install libssl.so.1.0.0 {}/usr/lib/libssl.so.1.0.0".format(get.installDIR()))
        shelltools.system("install libcrypto.so.1.0.0 {}/usr/lib/libcrypto.so.1.0.0".format(get.installDIR()))

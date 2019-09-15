#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

WorkDir="%s-%s/" % (get.srcNAME(), get.srcVERSION())
inarytools.cflags.add("-fno-strict-aliasing")

def setup():
    shelltools.cd("nss")
    shelltools.system('PATH="{}/path:$PATH" bash -x ./build.sh -v \
                      --opt --system-sqlite --system-nspr --enable-libpkix --disable-tests'.format(get.srcDIR()))

def build():
    shelltools.cd("nss")
    inarytools.dosed("coreconf/Linux.mk", " -shared ", " -Wl,-O1,--as-needed -shared ")
    if get.ARCH() == "x86_64":
        shelltools.export("USE_64", "1")
    shelltools.export("BUILD_OPT", "1")
    shelltools.export("NSS_ENABLE_ECC", "1")
    shelltools.export("NSS_USE_SYSTEM_SQLITE", "1")
    shelltools.export("NSPR_INCLUDE_DIR", "`nspr-config --includedir`")
    shelltools.export("NSPR_LIB_DIR", "`nspr-config --libdir`")
    shelltools.export("XCFLAGS", get.CFLAGS())

    # Use system zlib
    shelltools.export("PKG_CONFIG_ALLOW_SYSTEM_LIBS", "1")
    shelltools.export("PKG_CONFIG_ALLOW_SYSTEM_CFLAGS", "1")

    autotools.make("-C coreconf -j1")
    autotools.make("-C lib/dbm")
    autotools.make("-j1")

def install():
    for binary in ["certutil","nss-config","pk12util", "*util", "shlibsign", "signtool", "signver", "ssltap"]:
        inarytools.insinto("/usr/bin","dist/Linux*/bin/%s" % binary, sym=False)

    for lib in ["*.a","*.chk","*.so"]:
        inarytools.insinto("/usr/lib/nss","dist/Linux*/lib/%s" % lib, sym=False)

    # Headers
    for header in ["dist/private/nss/*.h","dist/public/nss/*.h"]:
        inarytools.insinto("/usr/include/nss", header, sym=False)

    # Drop executable bits from headers
    shelltools.chmod("%s/usr/include/nss/*.h" % get.installDIR(), mode=0o644)

    # Install nss-config and nss.pc
    inarytools.insinto("/usr/lib/pkgconfig", "nss/config/nss.pc")

    # create empty NSS database
    inarytools.dodir("/etc/pki/nssdb")
    shelltools.export("LD_LIBRARY_PATH", "%s/usr/lib/nss" % get.installDIR())
    shelltools.system("%s/usr/bin/modutil -force -dbdir \"sql:%s/etc/pki/nssdb\" -create" % (get.installDIR(), get.installDIR()))
    shelltools.chmod("%s/etc/pki/nssdb/*" % get.installDIR(), 0o644)
    shelltools.system('sed -i "s|%s||" %s/etc/pki/nssdb/*' % (get.installDIR(), get.installDIR()))

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
    shelltools.system("sed -i '/INSTALL_LIBS/s/libcrypto.a libssl.a//' Makefile")
    if get.buildTYPE() == "emul32":
        autotools.make(" install_sw DESTDIR=%s MANDIR=/usr/share/man" % get.installDIR())
    else:
        autotools.rawInstall("DESTDIR=%s MANDIR=/usr/share/man" % get.installDIR())

    if get.buildTYPE() == "emul32":
        #from distutils.dir_util import copy_tree
        shelltools.copytree("%s/emul32/lib32/" % get.installDIR(), "%s/usr/lib32" % get.installDIR())
        path = "%s/usr/lib32/pkgconfig" % get.installDIR()
        inarytools.dodir("/usr/lib32/openssl")
        inarytools.domove("/usr/lib32/engines-1.1", "/usr/lib32/openssl")
        for f in shelltools.ls(path): inarytools.dosed("%s/%s" % (path, f), "^(prefix=\/)_emul32", r"\1usr")
        inarytools.removeDir("/emul32")
        return

    # Rename conflicting manpages
    inarytools.rename("/usr/share/man/man1/passwd.1", "ssl-passwd.1")
    inarytools.remove("/usr/share/man/man1/openssl-passwd.1")
    inarytools.dosym("ssl-passwd.1", "/usr/share/man/man1/openssl-passwd.1")
    inarytools.rename("/usr/share/man/man1/rand.1", "ssl-rand.1")
    inarytools.remove("/usr/share/man/man1/openssl-rand.1")
    inarytools.dosym("ssl-passwd.1", "/usr/share/man/man1/openssl-rand.1")


    # Move engines to /usr/lib/openssl/engines
    inarytools.dodir("/usr/lib/openssl")

    # Certificate stuff
    inarytools.dobin("tools/c_rehash")


    # Create needed dirs
    for cadir in ["misc", "private"]:
        inarytools.dodir("/etc/ssl/%s" % cadir)

    inarytools.dohtml("doc/*")
    inarytools.dodoc("CHANGES*", "FAQ", "LICENSE", "NEWS", "README", "doc/*.txt")

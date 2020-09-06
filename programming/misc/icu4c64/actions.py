#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

WorkDir="icu-release-64-2/icu4c/source/"

def setup():
    autotools.autoconf("-f")
    options = "--with-data-packaging=library \
               --disable-samples \
               --disable-silent-rules"
    if get.buildTYPE() == "_emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=/_emul32/bin \
                     --sbindir=/_emul32/sbin"
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
    autotools.configure(options)
    inarytools.dosed("config/mh-linux", "-nodefaultlibs -nostdlib")

def build():
    autotools.make()

#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall('-j1 DESTDIR="%s"' % get.installDIR())
    if get.buildTYPE() == "_emul32":
        inarytools.domove("/_emul32/bin/icu-config", "/usr/bin", "icu-config-32")
        inarytools.removeDir("/_emul32")
        for f in shelltools.ls("%s/usr/lib32/pkgconfig" % get.installDIR()):
            inarytools.dosed("%s/usr/lib32/pkgconfig/%s" % (get.installDIR(), f), "_emul32", "usr")
        for i in ["libicudata.so","libicui18n.so","libicuio.so","libicutest.so","libicutu.so","libicuuc.so"]:
            inarytools.remove("/usr/lib32/"+i)
        inarytools.removeDir("/usr/lib32/icu")
        inarytools.removeDir("/usr/lib32/pkgconfig")
        return

    inarytools.dohtml("../*.html")
    inarytools.removeDir("/usr/bin")
    inarytools.removeDir("/usr/sbin")
    inarytools.removeDir("/usr/share")
    inarytools.removeDir("/usr/include")
    inarytools.removeDir("/usr/lib/icu")
    inarytools.removeDir("/usr/lib/pkgconfig")
    for i in ["libicudata.so","libicui18n.so","libicuio.so","libicutest.so","libicutu.so","libicuuc.so"]:
            inarytools.remove("/usr/lib/"+i)
        

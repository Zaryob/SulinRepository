#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import cmaketools
from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools


def setup():

    shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig" if get.buildTYPE() == "emul32" else  "/usr/lib/pkgconfig" )

    options = "-DCMAKE_BUILD_TYPE=Release   \
               -DCMAKE_INSTALL_PREFIX=/usr  \
               -DTESTDATADIR=$PWD/testfiles \
               -DENABLE_UNSTABLE_API_ABI_HEADERS=ON     \
               "

    cmaketools.configure(options)

def build():
    cmaketools.make()

def install():
    if get.buildTYPE() == "emul32":
        inarytools.insinto("/usr/lib32", "poppler/.libs/libpoppler.so*")
        inarytools.insinto("/usr/lib32", "glib/.libs/libpoppler-glib.so*")
        for f in ["poppler.pc", "poppler-glib.pc"]:
            inarytools.insinto("/usr/lib32/pkgconfig", f)
            inarytools.dosed("%s/usr/lib32/pkgconfig/%s" % (get.installDIR(), f), get.emul32prefixDIR(), get.defaultprefixDIR())
        return
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

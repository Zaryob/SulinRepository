#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-reentrant")

def build():
    autotools.make("shared")

    for t in ("fpack", "funpack", "imcopy", "fitscopy"):
        autotools.make(t)

    inarytools.dosed("cfitsio.pc", "\\$\\{prefix\\}/include", "${prefix}/include/%s" % get.srcNAME())

def check():
    autotools.make("testprog")

def install():
    for t in ("fpack", "funpack", "imcopy", "fitscopy"):
        inarytools.dobin(t)

    autotools.rawInstall("DESTDIR=%s LIBDIR=lib INCLUDEDIR=include/%s" % (get.installDIR(), get.srcNAME()))

    inarytools.remove("/usr/lib/*.a")

    inarytools.domove("/usr/lib/libcfitsio.so", "/usr/lib", "libcfitsio.so.0.0")
    inarytools.dosym("libcfitsio.so.0.0", "/usr/lib/libcfitsio.so.0")
    inarytools.dosym("libcfitsio.so.0.0", "/usr/lib/libcfitsio.so")

    inarytools.dodoc("*.txt", "README")

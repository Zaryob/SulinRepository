#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "espeak-%s-source" % get.srcVERSION()

def setup():
    # Build against portaudio v19
    shelltools.copy("src/portaudio19.h", "src/portaudio.h")

    # Remove binary voice dictionaries, we'll build them
    shelltools.system("rm -rf espeak-data/*_dict")

def build():
    autotools.make("-C src CXXFLAGS='%s' CFLAGS='%s' LDFLAGS='%s'" % (get.CXXFLAGS(), get.CFLAGS(), get.LDFLAGS()))

    shelltools.system("./compile-voices")

def install():
    shelltools.cd("src")
    autotools.rawInstall("DESTDIR=%s BINDIR=/usr/bin INCDIR=/usr/include/espeak LIBDIR=/usr/lib" % get.installDIR())
    shelltools.cd("..")

    inarytools.dodoc("ReadMe", "ChangeLog.txt", "License.txt")

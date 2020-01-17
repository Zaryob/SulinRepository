#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    inarytools.flags.add("-pthread -I/usr/include/OpenEXR -I/usr/include/libdrm")
    inarytools.ldflags.add("-lImath -lHalf -lIex -lIexMath -lIlmThread -lpthread")
    shelltools.system("./bootstrap")
    autotools.configure("--enable-shared \
                         --disable-static")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    # documents and examples go to "/usr/share/OpenEXR" without these parameters
    docdir = "/usr/share/doc/%s" % get.srcNAME()
    examplesdir = "%s/examples" % docdir
    autotools.rawInstall("DESTDIR=%s docdir=%s examplesdir=%s" % (get.installDIR(), docdir, examplesdir))

    inarytools.dodoc("AUTHORS", "ChangeLog","NEWS", "README.md","LICENSE")

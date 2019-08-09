#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import pythonmodules

def setup():
    inarytools.flags.add("-D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_GNU_SOURCE -fPIC")

    autotools.configure("--datadir=/usr/share/misc \
                         --disable-static \
                         --with-python=/usr/bin/python3 \
                         --enable-fsect-man5")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("python")
    pythonmodules.install(pyVer="3")

    shelltools.cd("..")
    inarytools.dodoc("ChangeLog", "MAINT", "README")

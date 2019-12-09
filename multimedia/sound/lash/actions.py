#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir = "lash-0.6.0.594"

def setup():
    shelltools.export("LDFLAGS", '-ldl -lm -ltirpc')
    autotools.configure("--with-python CFLAGS=-I/usr/include/tirpc")

def build():
    shelltools.export("LDFLAGS", '-ldl -lm -ltirpc')

    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for s in ("16", "24", "48", "96"):
        inarytools.dodir("/usr/share/icons/hicolor/%sx%s/apps" % (s, s))
        inarytools.domove("usr/share/lash/icons/lash_%spx.png" % s, "/usr/share/icons/hicolor/%sx%s/apps" % (s, s), "lash.png")

    inarytools.domove("usr/share/lash/icons/lash.svg", "/usr/share/icons/hicolor/scalable/apps")

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*", "TODO")

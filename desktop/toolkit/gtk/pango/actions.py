#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools


def setup():
    if get.buildTYPE()=="emul32":
        inarytools.dosed("pango/modules.c", "(pango\.modules)", r"\1-32")
    
    # autotools.autoreconf("-fiv")
    
    autotools.configure("--disable-static \
                         --sysconfdir=/etc \
                         --disable-gtk-doc \
                         --%sable-introspection" % ("dis" if get.buildTYPE()=="emul32" else "en"))

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE()=="emul32":
        #shelltools.move("pango/.libs/pango-querymodules", "pango/.libs/pango-querymodules-32")
        #inarytools.dobin("pango/.libs/pango-querymodules-32")
        return

    inarytools.dodir("/etc/pango")
    shelltools.touch(get.installDIR() +"/etc/pango/pango.modules")

    inarytools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "README", "NEWS")

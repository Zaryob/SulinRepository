#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -fPIC -fno-strict-aliasing -fPIE -DPIE " % get.CFLAGS())
    shelltools.export("LDFLAGS", "%s -pie -Wl,-z,now" % get.LDFLAGS())

    autotools.autoreconf("-fi")

    autotools.configure("--disable-static \
                         --disable-dependency-tracking \
                         --disable-rpath \
                         --localstatedir=/var \
                         --enable-slpv1 \
                         --enable-slpv2-security")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dohtml("doc/doc/html/*")
    inarytools.dodoc("AUTHORS", "FAQ", "ChangeLog", "NEWS", "README", "THANKS")

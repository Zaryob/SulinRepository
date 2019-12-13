#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import autotools
from inary.actionsapi import get


def setup():
   # autotools.autoreconf("-vfi")
    autotools.configure("--disable-dependency-tracking \
                         --disable-static \
                         --disable-migration \
                         --disable-maintainer-mode \
                         --with-modem-manager-1 \
                         --with-bluetooth \
                         --without-gnome \
                         --enable-more-warnings=yes \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --prefix=/usr \
                         --without-team \
                         --libexecdir=/usr/lib/NetworkManager \
                         --without-selinux")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("README", "COPYING")

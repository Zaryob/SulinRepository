#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("../configure \
                        --prefix=/usr \
                        --sysconfdir=/etc \
                        --disable-sanitizers")

def build():
    shelltools.cd("build")

    autotools.make("CPPFLAGS+=\"-U_FORTIFY_SOURCE\"")

def install():
    shelltools.cd("build")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

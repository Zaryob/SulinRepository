#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


def setup():
    inarytools.cflags.add(" -fno-builtin-strftime")
    autotools.configure("--prefix=/usr \
                         --disable-static \
                         --enable-liblightdm-gobject \
                           --with-libxklavier \
                            --enable-kill-on-sigterm \
                            --disable-libido \
                            --disable-libindicator \
                            --disable-static \
                         --disable-gtk-doc ")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

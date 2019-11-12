# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.autoreconf("-vif")

    autotools.configure("--disable-static \
                         --enable-unix-transport \
                         --enable-tcp-transport \
                         --enable-local-transport \
                         --enable-xpm-logos \
                         --enable-xdm-auth \
                         --with-pam \
                         --with-libaudit \
                         --with-xdmconfigdir=/etc/X11/xdm \
                         --with-default-vt=vt7 \
                         --with-config-type=ws \
                         --with-xft \
                         --with-pixmapdir=/usr/share/X11/xdm/pixmaps \
                        ")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodir("/var/lib/xdm")

    inarytools.dodoc("AUTHORS", "COPYING", "README")

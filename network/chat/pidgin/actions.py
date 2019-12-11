#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import perlmodules
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr \
                         --enable-dbus \
                         --enable-cyrus-sasl \
                         --enable-gnutls=yes \
                         --enable-nss=yes \
                         --enable-nm \
                         --enable-cap \
                         --disable-mono \
                         --disable-schemas-install \
                         --enable-meanwhile \
                         --disable-vv \
                         --enable-nm \
                         --enable-tcl \
                         --enable-tk \
                         --with-python=/usr/bin/python2.7 \
                         --x-includes=/usr/include/X11 \
                         --with-gnutls-includes=/usr/include/gnutls \
                         --with-gnutls-libs=/usr/lib \
                         --with-system-ssl-certs=/etc/ssl/certs")

    #inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dosym("../icons/hicolor/48x48/apps/pidgin.png", "/usr/share/pixmaps/pidgin.png")

    inarytools.dodoc("AUTHORS", "COPYING", "HACKING", "NEWS", "README", "ChangeLog")

    perlmodules.removePodfiles()

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
    #autotools.autoreconf("-fi")
    
    autotools.configure("--with-pam-module-dir=/lib/security/ \
                         --with-os-type=Sulin \
                         --with-mozjs=mozjs-17.0 \
                         --with-dbus \
                         --enable-examples \
                         --enable-introspection \
                         --enable-libsystemd-login=no \
                         --with-systemdsystemunitdir=no \
                         --disable-man-pages \
                         --disable-gtk-doc \
                         --disable-static")
    
    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ") 

def build():
    shelltools.export('HOME', get.workDIR())
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s/" % get.installDIR())

    inarytools.dodir("/var/lib/polkit-1")
    inarytools.dodoc("AUTHORS", "NEWS", "README", "HACKING", "COPYING")

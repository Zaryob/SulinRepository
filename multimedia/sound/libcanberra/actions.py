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
    autotools.autoreconf("-fi")
    autotools.configure("--disable-oss \
                         --disable-lynx \
                         --disable-gtk-doc \
                         --disable-schemas-install \
                         --enable-gstreamer \
                         --enable-gtk3 \
                         --enable-pulse \
                         --enable-alsa \
                         --enable-null \
                         --enable-tdb \
                         --with-builtin=dso \
                         --disable-static")
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    
    #inarytools.remove("/usr/lib/gtk-3.0/modules/libcanberra-gtk-module.so")
    inarytools.removeDir("/usr/share/gtk-doc")
    
    inarytools.dodoc("LGPL", "README")

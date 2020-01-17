#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import libtools
from inary.actionsapi import get

def setup():
    #autotools.autoreconf("-vfi")
    #libtools.libtoolize("--force --install")
    autotools.configure("--disable-doc \
                         --disable-static \
                         --disable-ruby \
                         --disable-csharp \
                         --disable-java \
                         --disable-cxx \
                         --disable-gl \
                         --enable-shared \
                         --enable-ncurses \
                         --enable-slang \
                         --enable-imlib2 \
                         --enable-x11 \
                         --with-x \
                         --x-libraries=/usr/lib")
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # we remove la files but symlinks stay there, so we remove by hand
    inarytools.remove("/usr/lib/*.la")
    #inarytools.removeDir("/usr/share/java")

    inarytools.dodoc("AUTHORS", "COPYING*", "ChangeLog", "NEWS","NOTES", "README", "THANKS")

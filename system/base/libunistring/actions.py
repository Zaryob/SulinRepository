#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.configure("--disable-static \
                         --disable-rpath")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    if get.buildTYPE()=="emul32":
        autotools.rawInstall("PREFIX=%s/emul32/usr" % get.installDIR())
        inarytools.dosym("libunistring.so.2.1.0", "/usr/lib32/libunistring.so.0")
        return
        
    autotools.install()

    inarytools.dosym("libunistring.so.2.1.0", "/usr/lib/libunistring.so.0")
    inarytools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "COPYING.LIB", "HACKING", "NEWS", "README",  "THANKS")

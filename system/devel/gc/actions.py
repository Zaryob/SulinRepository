#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    
    inarytools.flags.add("-std=gnu++98")
    #shelltools.system ("rm -rf libtool libtool.m4")
    
    autotools.configure("--disable-static \
                         --enable-cplusplus")
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("ChangeLog", "doc/README.linux", "doc/*.html")
    
    #inarytools.removeDir("/usr/share/gc")

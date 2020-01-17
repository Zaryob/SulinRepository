#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "libxml++-%s" % get.srcVERSION()

def setup():
    autotools.configure("--disable-static \
                         --disable-examples \
                         --enable-dependency-tracking")
    
    # for fix unused dependency
    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ") 
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dohtml("docs/reference/html/*")

    inarytools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README*")
    #inarytools.removeDir("/usr/share/doc/libxml++-2.6")

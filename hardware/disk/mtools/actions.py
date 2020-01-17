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
    #for i in ["mtools.texi"]:
    #    inarytools.dosed(i, "/usr/local/etc", "/etc")

    shelltools.export("INSTALL_PROGRAM", "install")
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr \
                        --sysconfdir=/etc/mtools \
                        --includedir=/usr/src/linux/include")

def build():
    autotools.make()
    inarytools.dosed("mtools.conf","SAMPLE FILE","#SAMPLE FILE")
def install():
    autotools.rawInstall('-j1 DESTDIR="%s"' % get.installDIR())
    

    inarytools.insinto("/etc/mtools","mtools.conf")
    
    inarytools.dodoc("COPYING", "README*", "Release.notes")

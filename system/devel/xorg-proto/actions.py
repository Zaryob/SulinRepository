# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.system("sed -i 's|$(datadir)/pkgconfig|$(libdir)/pkgconfig|g' Makefile.in")
    shelltools.system("sed -i 's|$(datadir)/pkgconfig|$(libdir)/pkgconfig|g' Makefile.am")
    
    autotools.autoreconf("-vif")
    autotools.configure("--prefix=/usr \
                         --docdir=/usr/share/doc/xorg-proto")
    
def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        
        
    inarytools.dodoc("README", "COPYING*", "AUTHORS")
    inarytools.domove("/usr/share/doc/xorg-proto/COPYING-*o","/usr/share/doc/xorg-proto/COPYING")
    

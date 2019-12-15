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
    inarytools.dosed("config/override.m4", "2.64", "2.69")
    shelltools.system('sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" libiberty/configure')
    autotools.configure(" \
                         --with-system-readline \
                         --with-separate-debug-dir=/usr/lib/debug \
                         --with-gdb-datadir=/usr/share/gdb \
                         --with-pythondir=/usr/lib/%s/site-packages \
                         --disable-nls \
                         --disable-rpath \
                         --with-python \
                         --with-expat" % get.curPYTHON())


def build():
    autotools.make()

def install():
    autotools.rawInstall('-C gdb DESTDIR="%s"' % get.installDIR())
    autotools.rawInstall('-C gdb/data-directory DESTDIR="%s"' % get.installDIR())
    
    # these are not necessary
    #for info in ["bfd","configure","standards"]:
        #inarytools.remove("/usr/share/info/%s.info" % info)
        
  
#    for hea in ["diagnostics","bfd_stdint","ansidecl","symcat","dis-asm", "bfd", "bfdlink", "plugin-api"]:
#        inarytools.remove("/usr/include/%s.h" % hea)
    
    inarytools.dodoc("README*", "MAINTAINERS", "COPYING*", "ChangeLog*")

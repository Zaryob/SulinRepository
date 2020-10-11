#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure('--prefix=/usr \
                        --libexecdir=/usr/lib/xfce4 \
                        --disable-static \
                        --disable-gsettings-backend')

    inarytools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    inarytools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    try:
        inarytools.dosym("libxfconf-0.so.3.0.0","/usr/lib/libxfconf-0.so.3")
        inarytools.dosym("libxfconf-0.so.3.0.0","/usr/lib/libxfconf-0.so")
    except Exception:
        print()
        
    
    inarytools.dodoc('AUTHORS', 'ChangeLog', 'NEWS', 'README', 'TODO', 'COPYING')


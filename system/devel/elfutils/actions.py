#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():

    # Remove -Wall from default flags. The makefiles enable enough warnings
    # themselves, and they use -Werror.
   
    
    options ='-disable-nls --program-prefix=\"eu-\" --with-zlib'
    
    if get.buildTYPE() == "emul32":
        shelltools.export("PKG_CONFIG_PATH","/usr/lib32/pkgconfig")
    
    elif get.ARCH() == "x86_64":
        inarytools.flags.add("-fexceptions")
        autotools.autoreconf("-vfi")

        inarytools.cflags.remove("-Wall")
        
        options +=" \
                    --enable-dwz \
                    --enable-thread-safety \
                    --with-bzlib \
                    --with-lzma"
    
    autotools.configure(options)

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        inarytools.remove("/usr/lib32/libelf.a")
        inarytools.remove("/usr/lib32/libasm.a")
        inarytools.remove("/usr/lib32/libdw.a")
        
        
    elif get.ARCH() == "x86_64":
    # Don't remove all the static libs as libebl.a is needed by other packages
        inarytools.remove("/usr/lib/libelf.a")
        inarytools.remove("/usr/lib/libasm.a")
        inarytools.remove("/usr/lib/libdw.a")

        inarytools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "NOTES", "README", "THANKS", "TODO")

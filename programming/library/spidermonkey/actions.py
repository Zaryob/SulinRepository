# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

shelltools.export("SHELL","/bin/sh")

def setup():
   shelltools.cd("js/src")
   
   autotools.configure("--prefix=/usr       \
                        --enable-readline   \
                        --enable-threadsafe \
                        --with-system-nspr")

def build():
    shelltools.cd("js/src")
    autotools.make()

def install():
    shelltools.cd("js/src")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
   
    
    inarytools.dodoc("README*")
    
    # add link for polkit
    inarytools.dosym("libmozjs-..so", "/usr/lib/libmozjs-17.0.so")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Lime GNU/Linux 2017
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import autotools , shelltools , get



def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--with-python3")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
 

    inarytools.domove("/usr/lib/libGLESv1_CM*", "/usr/lib/libglvnd/")
    inarytools.domove("/usr/lib/libEGL.so*", "/usr/lib/libglvnd/")
    inarytools.domove("/usr/lib/libGLESv2*", "/usr/lib/libglvnd/")
    inarytools.domove("/usr/lib/libGL.so*", "/usr/lib/libglvnd/")

    
    inarytools.dodoc("README.md")

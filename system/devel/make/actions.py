#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import get
from inary.actionsapi import inarytools

def setup():
    shelltools.system("sed -i '211,217 d; 219,229 d; 232 d' glob/glob.c")
    autotools.configure("--enable-nls \
                         --program-prefix=g")

def build():
    autotools.make()

#def check():
    #shelltools.export("LANG", "C")
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dosym("gmake", "/usr/bin/make")
    inarytools.dosym("gmake.1","/usr/share/man/man1/make.1")

    inarytools.dodoc("AUTHORS", "NEWS", "README*")

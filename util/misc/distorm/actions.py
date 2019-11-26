#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import pythonmodules

WorkDir="distorm-%s" % get.srcVERSION()

def setup():
    inarytools.dosed("setup.py", "'-Wall'", "'-Wno-strict-prototypes', '-Wno-missing-braces'")
    shelltools.system("sed -r 's|(CFLAGS	)=|\1+=|g' -i make/linux/Makefile")
    inarytools.dosed("make/linux/Makefile", "usr/local/lib", "%s/usr/lib" % get.installDIR())

def build():
    autotools.make("-C make/linux")
    pythonmodules.compile()

def install():
    inarytools.dodir("/usr/lib")
    autotools.rawInstall("-C make/linux PREFIX=/usr DESTDIR=%s" % get.installDIR())
    pythonmodules.install()
    inarytools.insinto("/usr/include/", "include/*.h")
    inarytools.dodoc("COPYING", "MANIFEST", "README*")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    #shelltools.sym("/bin/true", "%s/py-compile" % get.curDIR())

    if get.buildTYPE()=="emul32":
        shelltools.system("sed -i 's|use_python=auto|use_python=no|' configure.ac")
        shelltools.system("sed -i 's|use_python3=auto|use_python3=no|' configure.ac")

    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                        --with{}-python".format("out" if get.buildTYPE() == "emul32" else ""))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE()=="emul32":
        return

    inarytools.dodoc("ChangeLog", "COPYING*", "README", "NEWS")

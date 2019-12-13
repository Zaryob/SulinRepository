#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import pythonmodules
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir = "numpy-%s" % get.srcVERSION()

NUMPY_FCONFIG = "config_fc --fcompiler=gnu95"
f2py_docs = "%s/%s/f2py_docs" % (get.docDIR(), get.srcNAME())

shelltools.export("LDFLAGS", "%s -shared" % get.LDFLAGS())
shelltools.export("ATLAS", "None")
shelltools.export("PTATLAS", "None")

def build():
    pythonmodules.compile(NUMPY_FCONFIG)

def install():
    pythonmodules.install(NUMPY_FCONFIG)

    inarytools.remove("/usr/bin/f2py")
    inarytools.removeDir("/usr/share")
    inarytools.dodoc("LICENSE.txt", "THANKS.txt")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "Cython-%s" % get.srcVERSION()

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    inarytools.dodoc("COPYING*", "README*", "PKG-INFO")
    inarytools.domove("/usr/bin/cygdb","/usr/bin/cygdb3")
    inarytools.domove("/usr/bin/cythonize","/usr/bin/cythonize3")
    inarytools.domove("/usr/bin/cython","/usr/bin/cython3")


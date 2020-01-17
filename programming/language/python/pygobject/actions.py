#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir = "pygobject-%s" % get.srcVERSION()

def setup():
    # autoreconf is for under linking problem
    autotools.autoreconf("-fi")
    if get.buildTYPE()=="rebuild_python":
        shelltools.export("PYTHON", "/usr/bin/python3.7")
    else:
        shelltools.export("PYTHON", "/usr/bin/python2.7")
    autotools.configure("--disable-introspection")

def build():
    autotools.make()

def install():
    autotools.install()

    #shelltools.chmod("%s/usr/share/pygobject/xsl/fixxref.py" % get.installDIR(), 0755)
    inarytools.dodoc("AUTHORS", "NEWS", "ChangeLog", "README")

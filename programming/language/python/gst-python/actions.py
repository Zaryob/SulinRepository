#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

if get.buildTYPE()=="rebuild_python":
    buildir="build-python3"
    shelltools.export("PYTHON", "/usr/bin/python3.7")

else:
    buildir="build-python2"
    shelltools.export("PYTHON", "/usr/bin/python2.7")

def setup():

    autotools.autoreconf("-vfi")
    shelltools.makedirs(buildir)
    shelltools.cd(buildir)
    shelltools.system("../configure \
                           --localstatedir=/var \
                           --disable-api-docs \
                           --disable-html-docs \
                           --disable-static")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    shelltools.cd(buildir)

    autotools.make()

def install():
    shelltools.cd(buildir)

    autotools.install()

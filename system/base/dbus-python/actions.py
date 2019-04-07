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
    if get.buildTYPE()=="rebuild_python":
        shelltools.makedirs("build-python3")
    else:
        shelltools.makedirs("build-python2")
    autotools.autoreconf("-fi")

    if get.buildTYPE()=="rebuild_python":
        shelltools.cd("build-python3")
        shelltools.system("../configure PYTHON_VERSION=3 --prefix=/usr \
                               --localstatedir=/var \
                               --disable-api-docs \
                               --disable-html-docs \
                               --disable-static")
    else:
        shelltools.cd("build-python2")
        shelltools.system("../configure PYTHON_VERSION=2 -prefix=/usr \
                               --localstatedir=/var \
                               --disable-api-docs \
                               --disable-html-docs \
                               --disable-static")


    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    if get.buildTYPE()=="rebuild_python":
        shelltools.cd("build-python3")
    else:
        shelltools.cd("build-python2")
    autotools.make()

def check():
    #autotools.make("check")
    pass

def install():
    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")

    if get.buildTYPE()=="rebuild_python":
        shelltools.cd("build-python3")
    else:
        shelltools.cd("build-python2")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

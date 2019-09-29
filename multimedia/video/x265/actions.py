#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import inarytools
from inary.actionsapi import cmaketools
from inary.actionsapi import shelltools

def setup():
    shelltools.cd("source")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DENABLE_STATIC=OFF")

def build():
    shelltools.cd("source")
    cmaketools.make()

def install():
    shelltools.cd("source")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())


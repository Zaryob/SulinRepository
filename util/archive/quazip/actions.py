#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                                            -DBUILD_WITH_QT4:BOOL=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("COPYING", "README.txt", "NEWS.txt")

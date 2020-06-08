#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import qt
from inary.actionsapi import get

def setup():
    qt.configure()

def build():
    qt.make()

def install():
    qt.install("INSTALL_ROOT=%s" % get.installDIR())
    qt.install("INSTALL_ROOT=%s install_docs" % get.installDIR())


    #I hope qtchooser will manage this issue
    for bin in shelltools.ls("%s/usr/lib/qt5/bin" % get.installDIR()):
        inarytools.dosym("/usr/lib/qt5/bin/%s" % bin, "/usr/bin/%s-qt5" % bin)

    inarytools.insinto("/usr/share/licenses/qt5-wayland/", "LICENSE.*")

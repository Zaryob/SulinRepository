#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

NoStrip = "/"

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import qt
from inary.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "CXXFLAGS")
    qt.configure()

def build():
    qt.make()
    qt.make("docs")

def install():
    #inarytools.insinto("/usr/lib/qt5/qml", "qml/QtQml")
    #inarytools.insinto("/usr/lib/qt5/qml", "qml/Qt")
    #inarytools.insinto("/usr/lib/qt5/qml", "qml/QtQuick")
    #inarytools.insinto("/usr/lib/qt5/qml", "qml/QtQuick.2")
    #inarytools.insinto("/usr/lib/qt5/qml", "qml/QtTest")        
    qt.install("INSTALL_ROOT=%s install_docs" % get.installDIR())

    #I hope qtchooser will manage this issue
    for bin in shelltools.ls("%s/usr/lib/qt5/bin" % get.installDIR()):
        inarytools.dosym("/usr/lib/qt5/bin/%s" % bin, "/usr/bin/%s-qt5" % bin)

    inarytools.insinto("/usr/share/licenses/qt5-declarative/", "LICENSE*")

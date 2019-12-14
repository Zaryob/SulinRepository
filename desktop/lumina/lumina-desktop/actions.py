#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get
from inary.actionsapi import qt

def setup():
    shelltools.system('qmake-qt5 CONFIG+="configure WITH_I18N" QMAKE_CFLAGS_ISYSTEM= PREFIX=/usr QT5LIBDIR=/usr/lib/qt5 lumina.pro')

def build():
    qt.make()

def install():
    qt.install()
    inarytools.rename("/usr/man", "share/man")
    inarytools.dodoc("LICENSE","README*")

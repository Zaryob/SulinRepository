#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import qt
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


def setup():
    shelltools.system("sed -i -e 's/qdbusxml2cpp/qdbusxml2cpp-qt5/' src/signond/signond.pro")
    qt.configure(parameters="PREFIX=/usr LIBDIR=/usr/lib")

def build():
    qt.make()

def install():
    qt.install()

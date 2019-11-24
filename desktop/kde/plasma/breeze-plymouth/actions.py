#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import kde
from inary.actionsapi import inarytools

def setup():
    #inarytools.dosed("breeze/breeze.script", "kde.logo.png", "inary.logo.png")
    #inarytools.dosed("breeze/breeze.script", "Plasma 5.6", "INARYLinux")
    inarytools.dosed("breeze-text/breeze-text.plymouth.cmake", "Plasma @PROJECT_VERSION@", "INARYLinux")
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    inarytools.dodoc("COPYING", "README")

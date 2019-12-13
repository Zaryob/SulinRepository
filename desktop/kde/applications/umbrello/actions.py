#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import kde
from inary.actionsapi import get

NoStrip=["/usr/share"]

def setup():
    kde.configure("-DBUILD_KF5=ON")

def build():
    kde.make()

def install():
    kde.install()
    
    inarytools.dodoc("COPYING*", "AUTHORS", "CODING-STYLE", "ChangeLog", "README", "THANKS", "TODO")

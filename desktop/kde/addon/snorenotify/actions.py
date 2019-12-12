#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import kde
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    kde.configure("-DWITH_FREEDESKTOP_FRONTEND=ON")

def build():
    kde.make()

def install():
    kde.install()

    inarytools.dodoc("README*", "COPYING*")
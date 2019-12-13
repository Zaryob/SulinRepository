#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import kde
from inary.actionsapi import get

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install("DESTDIR={}".format(get.installDIR()))
    # Remove source build directory variable

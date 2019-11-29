#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import kde

NoStrip=["/usr/share"]

def setup():
    kde.configure("-DKMIX_KF5_BUILD=ON")

def build():
    kde.make()

def install():
    kde.install()
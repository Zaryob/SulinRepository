#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    mesontools.meson_configure("-D with-unity=disabled")

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get
#shelltools.export("HOME", get.workDIR())

def setup():
    mesontools.meson_configure("-Dvapi=true \
		-Ddemos=false")

def build():
    mesontools.ninja_build("-C build")

def install():
    mesontools.ninja_install("-C build")

    inarytools.dodoc("AUTHORS", "COPYING", "README")


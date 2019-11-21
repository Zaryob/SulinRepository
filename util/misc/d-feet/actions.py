#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Suleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import shelltools
from inary.actionsapi import mesontools
from inary.actionsapi import inarytools

def setup():
    mesontools.meson_configure()

def install():
    mesontools.ninja_build()
    inarytools.dodoc('README', 'AUTHORS', 'COPYING')

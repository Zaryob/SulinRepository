#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
   mesontools.meson_configure("-D alpm=false \
    -D gtk-doc=true \
    -D rpm=false")

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()

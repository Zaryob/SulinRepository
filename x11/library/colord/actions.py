#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import mesontools
from inary.actionsapi import inarytools

def setup():
    mesontools.meson_configure("-Ddaemon_user=colord             \
                                -Dvapi=true                      \
                                -Dsystemd=false                  \
                                -Dlibcolordcompat=true           \
                                -Dargyllcms_sensor=true          \
                                -Dudevrulesdir=/lib/udev/rules.d \
                                -Dbash_completion=true           \
                                -Ddocs=false                     \
                                -Dman=false                      \
                               ")

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()

    inarytools.dodoc("AUTHORS", "COPYING", "README.md")

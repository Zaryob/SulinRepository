#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import mesontools
from inary.actionsapi import shelltools

def setup():
    shelltools.system("echo \"4.3.0\"> .tarball-version")
    mesontools.meson_configure()

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()

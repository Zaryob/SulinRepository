#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import mesontools
from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    #folce-elogind iş başında olacak. o yüzden systemd açık bırakıyoz. yoksa derlenmiyo
    mesontools.meson_configure("-Dsystemd=true -Dsystemd_journal=false")

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()

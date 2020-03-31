#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    mesontools.meson_configure("-Dfuse=false      \
      -Dgphoto2=false   \
      -Dafc=false       \
      -Dbluray=false    \
      -Dnfs=false       \
      -Dmtp=false       \
      -Dsmb=false       \
      -Dtmpfilesdir=no  \
      -Ddnssd=false     \
      -Dgoa=false       \
      -Dgoogle=false    \
      -Dsystemd=false    \
      -Dsystemduserunitdir=no")

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()

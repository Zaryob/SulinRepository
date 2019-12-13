#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import mesontools
from inary.actionsapi import shelltools


def setup():
    shelltools.system("grep -rl '^#!.*python$' | xargs sed -i '1s/python/&3/'")
    mesontools.meson_configure("\
          -Dlibaudit=yes             \
          -Dlibpsl=true              \
          -Dnmtui=true               \
          -Dovs=true                 \
          -Dppp=true                 \
          -Dselinux=false            \
          -Dudev_dir=/lib/udev       \
          -Dsession_tracking=elogind \
          -Dmodem_manager=true       \
          -Dsystemdsystemunitdir=no  \
          -Dsystemd_journal=false    \
          -Dqt=false                 ")

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()

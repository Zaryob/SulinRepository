#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import mesontools
from inary.actionsapi import shelltools


def setup():
    shelltools.system("grep -rl '^#!.*python$' | xargs sed -i '1s/python/&3/'")
    shelltools.export("CXXFLAGS","-O2 -fPIC")
    mesontools.meson_configure("--prefix /usr              \
      --sysconfdir /etc          \
      --localstatedir /var       \
      -Djson_validation=false    \
      -Dlibaudit=no              \
      -Dlibpsl=false             \
      -Dnmtui=true               \
      -Dovs=true                 \
      -Diwd=true                 \
      -Dnm_cloud_setup=true      \
      -Dbluez5_dun=true          \
      -Debpf=true                \
      -Dppp=true                 \
      -Dselinux=false            \
      -Dudev_dir=/lib/udev       \
      -Dsession_tracking=elogind \
      -Dmodem_manager=false      \
      -Dsystemdsystemunitdir=no  \
      -Dsystemd_journal=false    \
      -Dqt=false")

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()

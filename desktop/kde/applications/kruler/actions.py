#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import kde

def setup():
    kde.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DBUILD_TESTING=OFF \
                    -DCMAKE_INSTALL_PREFIX=/usr \
                    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
                    -DECM_MKSPECS_INSTALL_DIR=/usr/lib/qt5/mkspecs/modules")

def build():
    kde.make()

def install():
    kde.install()
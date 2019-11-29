#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import kde
from inary.actionsapi import inarytools

def setup():
    kde.configure("-DCMAKE_BUILD_TYPE=Release \
                   -DCMAKE_INSTALL_PREFIX=/usr \
                   -DLIB_INSTALL_DIR=lib \
                   -DINCLUDE_DIR=/include/gtk-3.0/gtk \
                   -DLIBEXEC_INSTALL_DIR=lib \
                   -DSYSCONF_INSTALL_DIR=/etc \
                   -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
                   -DBUILD_TESTING=OFF")

def build():
    kde.make()

def install():
    kde.install()
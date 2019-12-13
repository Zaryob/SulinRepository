#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import kde

def setup():
    kde.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DCMAKE_INSTALL_PREFIX=/usr \
                    -DLIB_INSTALL_DIR=lib \
                    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON")

def build():
    kde.make()

def install():
    kde.install()

    inarytools.dodoc("COPYING",  "ChangeLog", "AUTHORS", "README", "COPYING-DOCS", "NEWS")

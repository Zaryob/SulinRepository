#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import kde

def setup():
    kde.configure("-DWITH_libshp=OFF \
                    -DWITH_libgps=OFF \
                    -DWITH_QextSerialPort=OFF \
                    -DWITH_liblocation=OFF \
                    -DBUILD_MARBLE_TOOLS=YES \
                    -DBUILD_TESTING=OFF \
                    -DBUILD_MARBLE_EXAMPLES=OFF \
                    -DBUILD_MARBLE_TESTS=OFF \
                    -DMOBILE=OFF")

def build():
    kde.make()

def install():
    kde.install()

    inarytools.dodoc("BUGS", "ChangeLog", "CODING", "COPYING*", "CREDITS", "LICENSE*", "MANIFESTO.txt", "USECASES")

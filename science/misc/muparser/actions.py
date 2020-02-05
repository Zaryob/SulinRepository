#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import cmaketools
from inary.actionsapi import get


def setup():
    cmaketools.configure('-DCMAKE_INSTALL_PREFIX=/usr \
		-DBUILD_SHARED_LIBS=ON \
		-DCMAKE_BUILD_TYPE=Release \
		-DBUILD_EXAMPLES=OFF \
		-DCMAKE_SKIP_RPATH=ON')

def build():
    autotools.make()


def install():
    autotools.install("DESTDIR=\""+get.installDIR()+"\"")

    inarytools.dodoc("Changes.txt", "License.txt")

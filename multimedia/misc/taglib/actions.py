#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    cmaketools.configure("-DBUILD_SHARED_LIBS=ON \
                        -DWITH_MP4=ON \
                        -DWITH_ASF=ON")

def build():
    cmaketools.make()

def install():
   cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

   inarytools.dodoc("AUTHORS","COPYING*")

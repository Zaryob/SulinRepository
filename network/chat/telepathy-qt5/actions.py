#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import autotools
from inary.actionsapi import get

WorkDir = "telepathy-qt-%s" % get.srcVERSION()

def setup():
    cmaketools.configure("-DDESIRED_QT_VERSION=5 \
                          -DPYTHON_EXECUTABLE=/usr/bin/python2.7 \
                          -DENABLE_EXAMPLES=OFF \
                          -DENABLE_TESTS=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

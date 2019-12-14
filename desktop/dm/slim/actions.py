#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    cmaketools.configure("  -DCMAKE_INSTALL_PREFIX=/usr \
                            -DCMAKE_BUILD_TYPE=Release \
                            -DCMAKE_SKIP_RPATH=ON \
                            -DUSE_PAM=yes \
                            -DUSE_CONSOLEKIT=no")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.removeDir("/lib/")

    inarytools.dodoc("COPYING","TODO", "README", "ChangeLog", "THEMES")

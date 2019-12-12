#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("PYTHON=/usr/bin/python3 \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DFCS_WITH_TEST_SUITE=OFF \
                          -DBUILD_STATIC_LIBRARY=OFF", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")

    inarytools.dodoc("AUTHORS.asciidoc", "COPYING.asciidoc", "NEWS.asciidoc", "README.asciidoc")

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
    inarytools.dosed("CMakeLists.txt", "LIB_SUFFIX 64", deleteLine="True")

    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DPYTHON_EXECUTABLE=/usr/bin/python2.7 \
                          -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
                          -DPYTHON_LIBRARY=/usr/lib/python2.7 \
                          -DCMAKE_SKIP_BUILD_RPATH=ON \
                          -DEXAMPLES=OFF -DFTDI_EEPROM=ON \
                          -DCMAKE_BUILD_TYPE=Release")


def build():
    autotools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #Remove python examples
    inarytools.removeDir("/usr/share/libftdi")

    # Their source can be useful though
    inarytools.dodoc("examples/*.c", destDir="%s/examples" % get.srcNAME())

    # Install udev rule
    inarytools.insinto("/lib/udev/rules.d", "packages/99-libftdi.rules")

    inarytools.doman("doc/man/man3/*.3")

    inarytools.dodoc("AUTHORS", "COPYING.LIB", "ChangeLog", "LICENSE", "README")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


def setup():
    shelltools.system('	sed -e "/torture_keyfiles/d" \
                		-i tests/unittests/CMakeLists.txt && \
                	    sed -e "/^check_include_file.*HAVE_VALGRIND_VALGRIND_H/s/^/#DONT /" \
                		-i ConfigureChecks.cmake')
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DWITH_GSSAPI=OFF", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()
    cmaketools.make("doc")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dohtml("doc/*")

    shelltools.cd("..")
    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "README")

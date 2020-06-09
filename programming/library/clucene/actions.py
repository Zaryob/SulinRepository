#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools


def setup():
    shelltools.system("	sed -i \
		-e '/ADD_SUBDIRECTORY (src\/ext)/d' \
		CMakeLists.txt && rm -rf src/ext")
    shelltools.export("CFLAGS", "-lpthread")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                    		-DENABLE_ASCII_MODE=OFF \
                    		-DENABLE_PACKAGING=OFF \
                    		-DDISABLE_MULTITHREADING=OFF \
                    		-DBUILD_CONTRIBS_LIB=ON \
                            -DLIB_DESTINATION:PATH=/usr/lib \
                            -DLUCENE_SYS_INCLUDES:PATH=/usr/lib \
                            -DDISABLE_MULTITHREADING=OFF", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()
    shelltools.cd("..")
    inarytools.dosym("/usr/lib/CLucene/clucene-config.h", "/usr/include/CLucene/clucene-config.h")

    inarytools.dodoc("AUTHORS","README","COPYING","ChangeLog")

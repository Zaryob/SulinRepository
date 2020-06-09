#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

paths = ["JavaScriptCore", "WebCore", "WebKit", "WebKit2"]
docs = ["AUTHORS", "COPYING.LIB", "THANKS", \
        "LICENSE-LGPL-2", "LICENSE-LGPL-2.1", "LICENSE"]

def setup():
    mesontools.cmake_configure("-DPORT=GTK \
                                -DCMAKE_SKIP_RPATH=ON \
                                -DENABLE_GTKDOC=OFF \
                                -DUSE_LIBHYPHEN=OFF \
                                -DENABLE_MINIBROWSER=ON")
def build():
    mesontools.ninja_build()
    mesontools.ninja_build('JavaScriptCore-4-gir')


def install():

    mesontools.ninja_install()
    inarytools.dodoc("NEWS")
    shelltools.cd("Source")
    for path in paths:
        for doc in docs:
            if shelltools.isFile("%s/%s" % (path, doc)):
                inarytools.insinto("%s/%s/%s" % (get.docDIR(), get.srcNAME(), path),
                                  "%s/%s" % (path, doc))

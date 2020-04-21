#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import cmaketools
from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

paths = ["JavaScriptCore", "WebCore", "WebKit", "WebKit2"]
docs = ["AUTHORS", "COPYING.LIB", "THANKS", \
        "LICENSE-LGPL-2", "LICENSE-LGPL-2.1", "LICENSE"]

def setup():
    shelltools.system("mkdir build")
    shelltools.cd("build")
    shelltools.system(" cmake \
    -DPORT=GTK \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_SKIP_RPATH=ON \
    -DENABLE_GTKDOC=ON \
    -DENABLE_MINIBROWSER=ON \
    -DLIBEXEC_INSTALL_DIR=/usr/lib \
    -DLIB_INSTALL_DIR=/usr/lib\
    -G Ninja ..")

def build():
    shelltools.cd("build")
    shelltools.system("ninja JavaScriptCore-4-gir")
    shelltools.system("ninja")

def install():
    shelltools.cd("build")
    shelltools.system("ninja installDESTDIR=%s" % get.installDIR())

    inarytools.dodoc("NEWS")
    shelltools.cd("Source")
    for path in paths:
        for doc in docs:
            if shelltools.isFile("%s/%s" % (path, doc)):
                inarytools.insinto("%s/%s/%s" % (get.docDIR(), get.srcNAME(), path),
                                  "%s/%s" % (path, doc))

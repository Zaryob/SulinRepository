#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import pythonmodules
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.export("PTHREAD_LIBS", "-lpthread")
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static")
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()
    shelltools.cd("python")
    pythonmodules.compile(pyVer="3")
    shelltools.cd("..")

def install():
    autotools.install()
    shelltools.cd("python")
    pythonmodules.install(pyVer="3")
    shelltools.cd("..")

    inarytools.insinto("/usr/share/vim/vimfiles/syntax/", "editors/proto.vim")
    inarytools.insinto("/usr/share/emacs/site-lisp/", "editors/protobuf-mode.el")

    inarytools.dodoc("CHANGES.txt", "CONTRIBUTORS.txt", "LICENSE", "README.md")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure(sourceDir="..")

def build():
    cmaketools.make("-C build")
    cmaketools.make("-C build doc")

def install():
    inarytools.dodoc("README", "TODO", "LICENSE")

    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.dohtml("doc/html/*")

    inarytools.remove("/usr/bin/lit2epub")

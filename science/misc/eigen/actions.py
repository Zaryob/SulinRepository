#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir = "eigen-eigen-323c052e1731/"

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure(sourceDir='..')

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    inarytools.dodoc("COPYING*")

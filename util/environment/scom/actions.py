#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#

from inary.actionsapi import cmaketools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import pythonmodules
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.cd("api")
    pythonmodules.compile(pyVer="3")
    shelltools.cd("../scom")
    cmaketools.configure()

def build():
    shelltools.cd("scom")
    autotools.make("VERBOSE=1")

def install():
    shelltools.cd("api")
    pythonmodules.install("--install-lib=/usr/lib/sulin", pyVer="3")
    shelltools.cd("../scom")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.dodir("/var/db")

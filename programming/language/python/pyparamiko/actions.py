#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir="paramiko-%s" % get.srcVERSION()

def setup():
    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s" % WorkDir,  "build_python3")
    shelltools.cd(WorkDir)

def build():
    pythonmodules.compile()

    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install()
    
    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.install(pyVer="3")

    for dirs in ["demos", "tests"]:
        inarytools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import inarytools
from inary.actionsapi import pythonmodules
from inary.actionsapi import get

def install():
    pythonmodules.install()
    pythonmodules.install(pyVer="3")
    inarytools.insinto("%s/%s/examples" % (get.docDIR(), get.srcNAME()),"examples/*")
    inarytools.dodoc("LICENSE", "CHANGES", "README.rst")

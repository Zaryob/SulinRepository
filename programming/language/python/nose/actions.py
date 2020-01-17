#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir = "nose-%s" % get.srcVERSION()

examples = "%s/%s/" % (get.docDIR(), get.srcNAME())

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

def setup():
    shelltools.system("sed -i -e 's:man/man1:share/man/man1:g' setup.py")

def build():
    pythonmodules.compile()
    pythonmodules.compile(pyVer="3")


def install():
    pythonmodules.install()
    pythonmodules.install(pyVer="3")

    inarytools.dohtml("doc/*")

    shelltools.chmod("examples/*", 0o644)
    inarytools.insinto(examples, "examples/*")

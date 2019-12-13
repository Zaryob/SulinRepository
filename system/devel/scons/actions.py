#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install("--no-version-script \
                           --optimize=1 \
                           --standalone-lib \
                           --install-scripts=/usr/bin \
                           --install-data=/usr/share", pyVer="3")
    shelltools.system("sed -i 's|env python|env python3|' {}/usr/bin/*".format(get.installDIR()))
    inarytools.dodoc("CHANGES*", "LICENSE*", "README*", "RELEASE*")

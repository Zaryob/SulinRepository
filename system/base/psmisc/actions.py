#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    autotools.configure("--bindir=/bin \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for file in shelltools.ls("%s/bin" % get.installDIR()):
        inarytools.dosym("/bin/%s" % file, "/usr/bin/%s" % file)

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")

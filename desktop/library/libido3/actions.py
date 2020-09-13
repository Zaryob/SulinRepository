#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir="ido-12.10.2"

def setup():
    shelltools.export("CFLAGS","-Wno-deprecated-declarations -Wno-error")
    autotools.configure("-prefix=/usr \
      --localstatedir=/var \
      --disable-tests")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR={}".format(get.installDIR()))

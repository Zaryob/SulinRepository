#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
import os

def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--enable-maintainer-mode --prefix=/usr")

def build():
    _env=os.environ.copy()
    os.environ.clear()
    os.system("make")
    os.environ.update(_env)

def install():
    autotools.install()

    inarytools.dodoc("ChangeLog","COPYING", "README")

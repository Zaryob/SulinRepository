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
    shelltools.system("./autogen.sh --prefix=/usr \
                        --with-xkb-bin-base=/usr/bin \
                        --with-xkb-base=/usr/share/X11/xkb \
                        --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("NEWS", "README", "CREDITS", "AUTHORS", "ChangeLog")

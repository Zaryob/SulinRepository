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
    autotools.configure("--prefix=/usr \
                         --libexecdir=/usr/lib \
                         --disable-static ")

def build():
    autotools.make()

def install():
    shelltools.system("make install DESTDIR={}".format(get.installDIR()))

    inarytools.dodoc('AUTHORS', 'ChangeLog', 'COPYING', 'HACKING', 'NEWS', 'STATUS', 'THANKS', 'TODO')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import get
from inary.actionsapi import inarytools

def setup():
    shelltools.system("autoreconf -fiv")
    autotools.configure("--prefix=/usr \
                         --with-cairo=system")

def build():
    autotools.make()

def install():
    autotools.make("install DESTDIR={}".format(get.installDIR()))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    shelltools.system("find -name '*.py' -exec sed -i '1s/python$/&2/' {} +")
    #shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--with-bdb=/usr")

def build():
    autotools.make()

def install():
    autotools.install()


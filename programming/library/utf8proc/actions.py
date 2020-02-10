#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    shelltools.system("sed 's:-D_BSD_SOURCE::' -i Makefile")

def build():
    autotools.make("PREFIX=/usr INCLUDEDIR=include \
		LIBDIR=lib COMPONENT_TYPE=lib-shared")

def install():
    autotools.install('PREFIX=/usr \
        INCLUDEDIR=include LIBDIR=lib \
        COMPONENT_TYPE=lib-shared install')


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure()

def build():
    autotools.make('CC="%s" \
                    CFLAGS="%s -O3 %s"' % (get.CC(), get.CFLAGS(), get.LDFLAGS()))

def install():
    inarytools.dobin("rzip")

    inarytools.doman("rzip.1")
    inarytools.dodoc("COPYING")

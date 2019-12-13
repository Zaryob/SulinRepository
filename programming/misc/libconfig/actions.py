#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Süleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--disable-static")

    # Do not link to unused m library
    inarytools.dosed("libtool", "^(postdeps=.*) -lm (.*)$", r"\1 \2")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("AUTHORS","ChangeLog","COPYING.LIB","README")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static --enable-unittest=no")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README", "COPYING")

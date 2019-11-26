#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

WorkDir = "unalz"

def build():
    autotools.make("linux-utf8")

def install():
    inarytools.dobin('unalz')
    inarytools.dodoc("readme.txt")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def build():
    shelltools.system("%s %s -o bchunk bchunk.c" % (get.CC(), get.CFLAGS()))

def install():
    inarytools.dobin("bchunk")

    inarytools.doman("bchunk.1")
    inarytools.dodoc("README", "COPYING", "ChangeLog")

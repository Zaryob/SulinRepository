#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    inarytools.dosed("Makefile","^CFLAGS.*","CFLAGS = %s -D_FILE_OFFSET_BITS=64" % get.CFLAGS())

def build():
    autotools.make()

def install():
    inarytools.dobin("lxsplit")

    inarytools.dodoc("README", "ChangeLog")

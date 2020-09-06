#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "mingetty-1.08"

def build():
    autotools.make('RPM_OPT_FLAGS="%s"' % get.CFLAGS())

def install():
    inarytools.dosbin("mingetty", "/sbin")
    inarytools.doman("mingetty.8")
    #inarytools.domo("tr.po", "tr", "mingetty.mo")

    inarytools.dodoc("COPYING")

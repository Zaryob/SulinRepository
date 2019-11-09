#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    autotools.make("-f makefile.shared")

def install():
    autotools.rawInstall("-f makefile.shared PREFIX=/usr DESTDIR=%s" % get.installDIR())
    inarytools.dodoc("changes.txt")

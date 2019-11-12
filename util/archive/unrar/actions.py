#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import autotools
from inary.actionsapi import get

WorkDir = "%s" % get.srcNAME()

def build():
#changed for version 4.2.4
    autotools.make()
#autotools.make for older version
#    autotools.make('-f makefile.unix \
#                    CXXFLAGS="%s" \
#                    CXX="%s" \
#                    STRIP="true"' % (get.CXXFLAGS(), get.CXX()))

def install():
    inarytools.dobin("unrar")

    inarytools.dodoc("readme.txt","license.txt")

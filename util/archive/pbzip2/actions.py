#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    autotools.make("CXX=%s" % get.CXX())

def install():
    inarytools.dobin("pbzip2")
    inarytools.doman("pbzip2.1")

    inarytools.dosym("pbzip2", "/usr/bin/pbunzip2")
    inarytools.dosym("pbzip2", "/usr/bin/pbzcat")

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

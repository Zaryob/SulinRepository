#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import get

def build():
    inarytools.dosed("Makefile", "prefix=.*", "prefix=%s" % get.defaultprefixDIR())
    autotools.make()

def install():
    autotools.install()

    inarytools.dodir("/etc")

    inarytools.dodoc("README", "ChangeLog")

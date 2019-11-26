#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    autotools.make()
    autotools.make("zstdmt")
    autotools.make("-C contrib/pzstd")

def install():
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s" % get.installDIR())
    inarytools.dobin("zstdmt")
    inarytools.dobin("contrib/pzstd/pzstd")
    inarytools.dodoc("LICENSE", "README*")

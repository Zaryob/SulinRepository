#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    autotools.make('CC="%s" \
                    CFLAGS="%s -fomit-frame-pointer -DLINUX -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64" \
                    LDFLAGS="%s"' % (get.CC(), get.CFLAGS(), get.LDFLAGS()))

def install():
    inarytools.dobin("tree")

    inarytools.doman("doc/tree.1")
    inarytools.dodoc("CHANGES", "README*")

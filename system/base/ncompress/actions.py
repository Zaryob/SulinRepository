#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    shelltools.move("Makefile.def", "Makefile")
    autotools.make("-f Makefile CFLAGS='%s -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE'" % get.CFLAGS())

def install():
    inarytools.dobin("compress")
    inarytools.dosym("compress", "/usr/bin/uncompress")

    inarytools.doman("compress.1")
    inarytools.dosym("compress.1", "/usr/share/man/man1/uncompress.1")

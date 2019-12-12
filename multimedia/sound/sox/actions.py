#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -fsigned-char -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static \
                         --with-gsm \
                         --with-dyn-default")

    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("ChangeLog", "README", "NEWS", "AUTHORS", "COPYING", "LICENSE*")

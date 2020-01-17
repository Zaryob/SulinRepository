#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2006 - 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

shelltools.export("MONO_SHARED_DIR", get.workDIR())

def setup():
    autotools.configure("--disable-static\
                         --enable-largefile")

    inarytools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("ChangeLog", "COPYING", "README", "TODO")

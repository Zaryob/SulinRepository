#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    inarytools.dobin("less")
    inarytools.dobin("lessecho")
    inarytools.dobin("lesskey")
    inarytools.newman("lesskey.nro", "lesskey.1")
    inarytools.newman("less.nro", "less.1")

    inarytools.dodoc("NEWS", "README", "COPYING")

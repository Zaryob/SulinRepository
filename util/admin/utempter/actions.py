#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def build():
    inarytools.dosed("Makefile", "INSTALL.*?STATICLIB", deleteLine=True)
    autotools.make('libdir="/usr/lib" libexecdir="/usr/libexec"')

def install():
    autotools.rawInstall('DESTDIR="%s" libdir="/usr/lib" libexecdir="/usr/libexec"' % get.installDIR())

    inarytools.dodoc("COPYING", "README")
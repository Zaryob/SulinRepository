#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Suleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr --bindir=/bin")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    inarytools.dosym("tcsh", "/bin/csh")

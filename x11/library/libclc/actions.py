#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Suleyman POYRAZ (Zaryob)
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get




def setup():
    shelltools.system("PYTHON=%s ./configure.py  --prefix=/usr")


def build():
    autotools.make()

def install():
    autotools.install("DESTDIR=%s" % get.installDIR())

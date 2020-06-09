#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Suleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    autotools.make()

def install():
    inarytools.makedirs("{}/usr/sbin/".format(get.installDIR()))
    autotools.rawInstall("DESTDIR={}".format(get.installDIR()))

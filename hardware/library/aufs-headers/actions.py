#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Suleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def install():
    inarytools.insinto("/usr/include/linux", "include/linux/aufs_type.h")

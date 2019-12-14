#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Suleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def check():
    autotools.make("test")

def install():
    autotools.install()

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")

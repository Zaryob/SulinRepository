#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("TODO", "README", "NEWS", "ChangeLog", "AUTHORS")

#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.configure("BASH=/bin/bash")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

    inarytools.dodoc("ChangeLog", "NEWS", "FAQ", "README", "AUTHORS", "doc/*")

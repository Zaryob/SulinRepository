#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import perlmodules
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make()

def install():
    perlmodules.install()

    inarytools.dodoc("Changes", "README.md")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import pythonmodules
from inary.actionsapi import inarytools

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    inarytools.dodoc("AUTHORS.*", "CHANGELOG.*", "LICENSE", "README.*")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    shelltools.system("sed 's/FUNC_FFLUSH_STDIN/-1/g' -i lib/fseeko.c")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.doman("doc/*.[15]")
    inarytools.dodoc("ABOUT*", "AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "THANKS", "TODO")

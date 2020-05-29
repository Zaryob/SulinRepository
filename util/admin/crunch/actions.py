#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import get
from inary.actionsapi import inarytools

    
def build():
    autotools.make()

def install():
    inarytools.dobin("crunch")
    inarytools.dodoc("COPYING")
    inarytools.doman("crunch.1")
    inarytools.insinto("/usr/share/crunch/", "charset.lst")

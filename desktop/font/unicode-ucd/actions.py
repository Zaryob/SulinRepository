#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import libtools
from inary.actionsapi import get

WorkDir = "."

def install():
    
    inarytools.insinto("/usr/share/unicode/ucd", "*")
    
    inarytools.remove("/usr/share/unicode/ucd/inaryBuildState")


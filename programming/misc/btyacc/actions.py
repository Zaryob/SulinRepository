# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir = "."

def setup():
    inarytools.dosed("main.c", "len + 13", "len + 14")

def build():
    autotools.make()

def install():
    inarytools.dobin("btyacc")
    inarytools.newman("manpage", "btyacc.1")
    inarytools.dodoc("README*")

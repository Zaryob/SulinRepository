# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools


def build():
    autotools.make()

def install():
    inarytools.dobin("b43-fwcutter")

    inarytools.dodoc("COPYING", "README")
    inarytools.doman("*.1")

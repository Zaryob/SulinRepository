# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("ChangeLog", "COPYING", "README")

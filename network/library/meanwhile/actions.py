# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--enable-doxygen=no \
                         --enable-static=no \
                         --disable-mailme")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("README", "ChangeLog", "AUTHORS", "COPYING", "LICENSE", "TODO")

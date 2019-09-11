#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

shelltools.export('HOME', get.workDIR())
def setup():
    autotools.configure("--disable-static \
                         --disable-gtk-doc \
                         --enable-maintainer-flags=no \
                         --enable-introspection=yes")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")

#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "glade3-%s" % get.srcVERSION()

def setup():
    autotools.configure("PYTHON=/usr/bin/python3 \
                         --disable-static \
                         --enable-gtk-doc")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    inarytools.dodoc("AUTHORS", "COPYING*", "ChangeLog", "NEWS", "README", "TODO")

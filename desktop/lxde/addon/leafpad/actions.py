#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.configure("--disable-dependency-tracking \
                         --enable-chooser \
                         --enable-print")

def build():
    autotools.make()

def install():
    autotools.install()
    inarytools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")


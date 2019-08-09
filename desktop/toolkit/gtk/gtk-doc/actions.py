#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licences/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    autotools.configure("--disable-static --disable-scrollkeeper")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("AUTHORS", "MAINTAINERS", "ChangeLog", "README", "NEWS", "TODO")

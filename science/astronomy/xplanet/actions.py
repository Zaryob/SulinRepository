#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.configure("--prefix=/usr \
                         --with-xscreensaver \
                         --with-freetype \
                         --with-pango \
                         --with-cspice \
                         --with-gif \
                         --with-jpeg \
                         --with-png \
                         --with-pnm \
                         --with-tiff")


def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "TODO")

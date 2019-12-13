#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import autotools

def setup():
    #autotools.autoreconf("-vfi")
    autotools.configure("--prefix=/usr \
                         --enable-pinentry-curses \
                         --enable-pinentry-gtk3 \
                         --disable-pinentry-qt \
                         --enable-pinentry-gtk2 \
                         --disable-pinentry-qt4 \
                         --enable-fallback-curses")

def build():
    autotools.make()

def install():
    autotools.install()

    # We're using pinentry-wrapper as additional file instead of upstream pinentry symlink.
    inarytools.remove("/usr/bin/pinentry")

    inarytools.dosym("pinentry-gtk-2", "/usr/bin/pinentry-gtk")
    #inarytools.dosym("pinentry-qt4", "/usr/bin/pinentry-qt")

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS")

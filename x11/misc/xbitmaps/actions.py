# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    # Fix conflict with xorg-app
    inarytools.remove("/usr/include/X11/bitmaps/black6")
    inarytools.remove("/usr/include/X11/bitmaps/box6")

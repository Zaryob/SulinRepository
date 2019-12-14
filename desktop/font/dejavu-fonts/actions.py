#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl-3.0.txt

from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import autotools
from inary.actionsapi import get


def build():
    autotools.make('FC-LANG="" BLOCKS="/usr/share/unicode/ucd/Blocks.txt" UNICODEDATA="/usr/share/unicode/ucd/UnicodeData.txt"')

def check():
    autotools.make("check")

def install():
    inarytools.insinto("/usr/share/fonts/dejavu", "build/*.ttf")

    # Create symlinks for fontconfig files
    for conf in shelltools.ls("fontconfig"):
        inarytools.insinto("/etc/fonts/conf.avail", "fontconfig/%s" % conf)
        inarytools.dosym("/etc/fonts/conf.avail/%s" % conf, "/etc/fonts/conf.d/%s" % conf)


    inarytools.dosym("/usr/share/fonts/dejavu" , "/etc/X11/fontpath.d/dejavu")

    inarytools.dodoc("AUTHORS", "LICENSE", "NEWS")

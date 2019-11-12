#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "%s/.dropbox-dist" % get.ARCH()
NoStrip = "/opt/dropbox/library.zip"

def install():
    #inarytools.dodir("/opt/dropbox")
    inarytools.insinto("/opt/dropbox", "*")

    # Arch removes this lib, Pardus libgcc package provides libstdc++.so.6
    #inarytools.remove("/opt/dropbox/libstdc++.so.6")

    inarytools.dodoc("VERSION")        
    inarytools.remove("/opt/dropbox/VERSION")

    # you can remove these lines if u don't like monochromatic systemtry icons
    # i'm going to try find a way to make this optional
    #inarytools.insinto("/opt/dropbox/icons/hicolor/16x16/status", "../../hede/*.png")

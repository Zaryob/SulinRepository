#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools


def install():
    inarytools.insinto("/usr/share/fonts/noto", "unhinted/Noto*/*.ttf")
    inarytools.insinto("/usr/share/fonts/noto", "hinted/Noto*/*.ttf")
    inarytools.insinto("/usr/share/fonts/croscore", "hinted/Arimo/*.ttf")
    inarytools.insinto("/usr/share/fonts/croscore", "hinted/Tinos/*.ttf")
    inarytools.insinto("/usr/share/fonts/croscore", "hinted/Cousine/*.ttf")


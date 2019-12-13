#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "rootactions_servicemenu_%s" % get.srcVERSION()

def install():
    inarytools.insinto("/usr/share/kservices5/ServiceMenus", "Root_Actions_%s/dolphin-KDE4/*.desktop" % get.srcVERSION())
    inarytools.dobin("Root_Actions_%s/rootactions-servicemenu.pl" % get.srcVERSION())

    inarytools.dodoc("README")
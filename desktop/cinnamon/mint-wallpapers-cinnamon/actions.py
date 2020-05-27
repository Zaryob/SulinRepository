#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get



def install():
    shelltools.system("""mkdir -p {0}/usr/share/backgrounds/linuxmint-tessa
	cp -a {1}/mint-backgrounds-*/backgrounds/linuxmint-* {0}/usr/share/backgrounds/
	mkdir -p {0}/usr/share/gnome-background-properties
	mkdir -p {0}/usr/share/cinnamon-background-properties
	cp -a {1}/mint-backgrounds-*/cinnamon-background-properties/* {0}/usr/share/cinnamon-background-properties/
	cp -a {1}/mint-backgrounds-*/gnome-background-properties/* {0}/usr/share/gnome-background-properties""".format(get.installDIR(),get.workDIR()))


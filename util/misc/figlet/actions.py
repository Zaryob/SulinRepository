#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    autotools.make()

def install():
    autotools.rawInstall("BINDIR=/usr/bin MANDIR=/usr/share/man \
              DEFAULTFONTDIR=/usr/share/figlet/fonts\
              DESTDIR=%s" % get.installDIR())
    inarytools.dodoc("CHANGES", "FAQ", "figfont.txt", "LICENSE", "README")

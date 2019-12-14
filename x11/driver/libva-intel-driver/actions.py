# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    inarytools.dosed("configure.ac", "gen4asm=yes", "gen4asm=no")
    autotools.autoreconf("-vif")
    autotools.configure("\
                         --disable-silent-rules \
                         --disable-wayland \
                        ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("COPYING")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoreconf()
    autotools.configure("--disable-static \
                         --sysconfdir=/etc/aspell \
                         --enable-docdir=/usr/share/doc/%s" % get.srcNAME())

    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # install ispell/spell compatibility scripts
    inarytools.insinto("/usr/bin","scripts/ispell","ispell-aspell")
    inarytools.insinto("/usr/bin","scripts/spell", "spell-aspell")

    inarytools.dodoc("README*", "TODO")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.system("sed -i '/skipping/d' util/packer.c")
    autotools.autoreconf("-vfi")
    autotools.configure("--with-default-dict=/usr/share/cracklib/pw_dict \
                         --prefix=/usr    \
                         --with-python=/usr/bin/python3 \
                         --disable-static")

    # for unused
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("all")

def install():
    autotools.install()

    # Create dictionary files
    #shelltools.system("cat /usr/share/cracklib/cracklib-small|%s/usr/sbin/cracklib-packer %s/usr/share/cracklib/pw_dict" % (get.installDIR(),get.installDIR()))

    inarytools.domo("po/tr.po","tr","cracklib.mo")
    inarytools.dodoc("ChangeLog", "README*", "NEWS", "COPYING.LIB", "AUTHORS")

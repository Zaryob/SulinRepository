# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    inarytools.flags.add("-DNDEBUG")

    autotools.autoreconf("-vfi")
    autotools.configure("PYTHON=/usr/bin/python3 \
                         --disable-static \
                         --enable-xevie \
                         --enable-xprint \
                         --enable-xinput \
                         --enable-xkb \
                         --without-launchd \
                         --without-doxygen")

    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("-j1 DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("COPYING", "NEWS", "README.md")

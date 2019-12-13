#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#
# taken from
# svn://svn.mplayerhq.hu/dvdnav/trunk/libdvdread

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import libtools
from inary.actionsapi import get

def setup():
    libtools.libtoolize("--force --install")
    autotools.autoreconf("-vfi")

    autotools.configure("--with-libdvdcss=/usr \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    inarytools.dodoc("ChangeLog", "AUTHORS", "README", "TODO")


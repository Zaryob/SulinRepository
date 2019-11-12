#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-shared \
                         --disable-static")

def build():
    autotools.make('OPT_CFLAGS=""')

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    inarytools.remove("/usr/lib/*.a")

    # FIXME: avidemux needs this
    # inarytools.insinto("/usr/include","libdts/dca_internal.h")

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO", "doc/libdca.txt")


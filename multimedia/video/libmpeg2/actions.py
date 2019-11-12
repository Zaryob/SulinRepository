#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import libtools
from inary.actionsapi import get


def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-shared \
                         --disable-dependency-tracking \
                         --disable-static \
                         --disable-sdl \
                         --without-x")

def build():
    autotools.make('OPT_CFLAGS="%s" \
                    MPEG2DEC_CFLAGS="%s" \
                    LIBMPEG2_CFLAGS=""' % (get.CFLAGS(), get.CFLAGS()))

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")

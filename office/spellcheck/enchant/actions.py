#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-fvi")
    autotools.configure("--disable-static \
                         --enable-aspell \
                         --enable-zemberek \
                         --enable-myspell \
                         --with-myspell-dir=/usr/share/hunspell \
                         --disable-ispell \
                         --disable-uspell \
                         --disable-hspell")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "NEWS", "README")

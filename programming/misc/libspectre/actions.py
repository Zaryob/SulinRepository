#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --enable-test \
                         --disable-dependency-tracking \
                         --with-gnu-ld")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    inarytools.dodoc("ChangeLog","COPYING","NEWS","README")

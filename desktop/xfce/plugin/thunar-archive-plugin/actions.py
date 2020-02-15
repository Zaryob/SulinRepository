#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import get
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    #shelltools.export("LDFLAGS", "%s -lgtk-x11-2.0 -lthunarx-2" % get.LDFLAGS())
    autotools.configure("--disable-static \
                        --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

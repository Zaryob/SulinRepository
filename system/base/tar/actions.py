#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-vfi")

    # For being able to build as root, pff
    shelltools.export("FORCE_UNSAFE_CONFIGURE", "1")
    autotools.configure("--bindir=/bin \
                         --libexecdir=/bin \
                         --disable-rpath \
                         --enable-nls")

def build():
    autotools.make()

# test has a sandbox problem disabled.
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.doman("doc/tar.1")

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*", "THANKS")


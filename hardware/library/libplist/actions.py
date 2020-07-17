#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import inarytools
from inary.actionsapi import autotools

def setup():
    #  do not link with installed old library
    inarytools.dosed("cython/Makefile.*", "(plist_la_LDFLAGS\s=.*)(\s-L\$\(libdir\))(.*)", r"\1\3")

    autotools.configure("\
                         --disable-static \
                         --disable-silent-rules \
                        ")

    inarytools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "COPYING", "COPYING.LESSER", "README.md")

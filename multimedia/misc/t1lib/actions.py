#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    inarytools.dosed("doc/Makefile.in", "dvips", "#dvips")
    inarytools.dosed("xglyph/xglyph.c", "\./\(t1lib\.config\)", "/etc/t1lib/\1")

    autotools.configure("--datadir=/etc \
                         --with-x \
                         --enable-static=no")


def build():
    autotools.make("without_doc")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("Changes", "README*")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


def setup():
    cflags = "%s -fPIC" % get.CFLAGS()
    shelltools.export("CFLAGS", cflags)

    autotools.configure("--disable-static")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall('DESTDIR=%s man1dir=/usr/share/man/man1' % get.installDIR())

    inarytools.dohtml("doc/*")
    inarytools.dodoc("Changes", "README.md")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    # thanks alpine linux
    shelltools.system("sed 's|/usr/bin/sh|/bin/sh|' \
		-i build-aux/compile \
		-i build-aux/missing \
		-i build-aux/install-sh \
		-i build-aux/depcomp \
		-i build-aux/config.sub \
		-i build-aux/config.guess")
    shelltools.system("./configure --prefix=/usr \
		--sysconfdir=/etc \
		--mandir=/usr/share/man \
		--localstatedir=/var")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

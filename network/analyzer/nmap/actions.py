#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get
shelltools.export("PYTHON","python2")

def setup():
    autotools.autoconf()
    autotools.configure("--prefix=/usr \
		--without-zenmap\
		--libexecdir=/usr/libexec \
		--mandir=/usr/share/man \
		--with-libpcap=included ")

def build():
    shelltools.system("set +u")
    autotools.make()
    shelltools.system("set -u")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

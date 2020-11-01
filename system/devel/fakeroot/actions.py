#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import get
from inary.actionsapi import inarytools

def setup():
    shelltools.system("./bootstrap")
    autotools.configure("--prefix=/usr \
    --libdir=/usr/lib/libfakeroot \
    --disable-static \
    --with-ipc=sysv")

def build():
    autotools.make()
    shelltools.cd("doc")
    shelltools.system("po4a -k 0 --rm-backups --variable 'srcdir=../doc/' po4a/po4a.cfg")

#def check():
    #shelltools.export("LANG", "C")
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

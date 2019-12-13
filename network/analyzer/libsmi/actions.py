#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

pibsdir = "/usr/share/pibs"

def setup():
    shelltools.export("CFLAGS", "%s -O2" % get.CFLAGS())

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --enable-shared \
                         --enable-smi \
                         --enable-sming")

def build():
    autotools.make()

def check():
    shelltools.export("LC_ALL", "C")
    autotools.make("-j1 check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.removeDir(pibsdir)
    for i in ["ietf", "site", "tubs"]:
        inarytools.insinto(pibsdir, "pibs/%s" % i)
        inarytools.remove("%s/%s/Makefile*" % (pibsdir, i))

    inarytools.dodoc("smi.conf-example", "ANNOUNCE", "ChangeLog", "README", "THANKS", "TODO", "doc/*.txt", "doc/smi*")


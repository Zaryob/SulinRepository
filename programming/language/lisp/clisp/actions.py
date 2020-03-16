#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import get
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    autotools.rawConfigure("--prefix=/usr --with-readline --with-ffcall src")
def build():
    shelltools.cd("src")
    shelltools.system("./makemake --prefix=/usr --with-readline --with-ffcall --with-dynamic-ffi > Makefile")
    shelltools.system("make")

def install():
    shelltools.cd("src")
    autotools.make("-j1 DESTDIR=%s prefix=/usr install-bin" % (get.installDIR()))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static \
                         --enable-gtk \
                         --with-gtk=3.0 \
                         --disable-orbit \
                         --enable-silent-rules")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #workaround to run gnome-shell
    inarytools.remove("/usr/lib/girepository-1.0/GConf-2.0.typelib")

    inarytools.dodoc("README", "COPYING", "TODO", "NEWS", "ChangeLog", "AUTHORS")

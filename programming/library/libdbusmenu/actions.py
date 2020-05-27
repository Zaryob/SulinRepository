#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Süleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.export("HAVE_VALGRIND_TRUE","#")
    shelltools.export("HAVE_VALGRIND_FALSE","")
    shelltools.export("CFLAGS"," -Wno-error")
    autotools.configure("--disable-{dumper,static,tests} \
                        --with-gtk=3")

def build():
    autotools.make()

"""
#Requires dbus-test-runner (https://launchpad.net/dbus-test-runner)

def check():
    autotools.make("check")
"""

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "COPYING*", "README", "NEWS")

    inarytools.removeDir("/usr/share/gtk-doc")

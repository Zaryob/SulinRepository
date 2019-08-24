#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


flags = "%s -fPIC" % get.CFLAGS() if get.ARCH() == "x86_64" else get.CFLAGS()

def setup():
    shelltools.export("CFLAGS", flags)
    
    shelltools.system("./autogen.sh")

    autotools.configure("--enable-nls \
                         --disable-rpath")
                         # --enable-python \
                         # --enable-python-bindings \

def build():
    autotools.make()

# FIXME: python tests fail, others fail in 64bit, gentoo says tests are wrong
def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "BSD.txt", "GNU_GPL-2.0", "GNU_LGPL-2.0", "Artistic.txt")


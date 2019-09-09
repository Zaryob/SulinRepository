#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.configure("--disable-static \
                         --disable-silent-rules")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

# solve conflict with elfutils and glibc-devel
#    inarytools.remove("/usr/include/nlist.h")
#    inarytools.remove("/usr/lib/libbsd.a")

    inarytools.dodoc("ChangeLog", "COPYING", "README", "TODO")

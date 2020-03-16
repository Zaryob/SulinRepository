#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --enable-shared")

def build():
    autotools.make("-j1")

def install():
    inarytools.dodir("/usr/share")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.domove("/usr/share/html/", "/usr/share/doc/%s/" % get.srcNAME())

    inarytools.remove("/usr/lib/*.a")

    inarytools.dodoc("COPYING", "NEWS", "README")

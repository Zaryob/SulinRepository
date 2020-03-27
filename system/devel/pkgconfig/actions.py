#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

#WorkDir = "pkg-config-%s" % get.srcVERSION()

def setup():
    autotools.configure("--with-pc-path=/usr/lib/pkgconfig:/usr/share/pkgconfig:/usr/lib/x86_64-pc-linux-gnu/pkgconfig:/usr/local/lib/pkgconfig:/lib/pkgconfig")

#def check():
#    autotools.make("check")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodir("/usr/lib/pkgconfig")
    inarytools.dodir("/usr/share/pkgconfig")

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")

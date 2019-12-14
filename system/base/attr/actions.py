#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

suffix = "32" if get.buildTYPE() == "emul32" else ""
bindir = "/tmp"  if get.buildTYPE() == "emul32" else "/bin"

def setup():
    autotools.rawConfigure("--libdir=/lib%s \
                            --sysconfdir=/etc \
                            --disable-static  \
                            --mandir=/usr/share/man \
                            --libexecdir=/lib%s \
                            --bindir=%s" % (suffix, suffix, bindir))
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        shelltools.copytree("%s/lib32/pkgconfig" % get.installDIR(), "%s/usr/lib32/pkgconfig" % get.installDIR())
        inarytools.removeDir("/tmp")
        inarytools.removeDir("/lib32/pkgconfig")
        return
    shelltools.copytree("%s/lib/pkgconfig" % get.installDIR(), "%s/usr/lib/pkgconfig" % get.installDIR())
    inarytools.removeDir("/lib/pkgconfig")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def build():
    shelltools.cd("libraries/liblmdb")
    autotools.make("prefix=/usr")

def install():
    shelltools.cd("libraries/liblmdb")
    
    inarytools.dodir("/usr/bin")
    inarytools.dodir("/usr/lib")
    inarytools.dodir("/usr/man/man1")
    inarytools.dodir("/usr/share")
    inarytools.dodir("/usr/include")
    
    autotools.rawInstall("DESTDIR=%s prefix=/usr" % get.installDIR())
    
    inarytools.domove("/usr/man", "/usr/share")
    inarytools.dodoc("LICENSE", "CHANGES", "COPYRIGHT")

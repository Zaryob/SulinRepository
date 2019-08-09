#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    inarytools.flags.add("-fPIC -D_GNU_SOURCE")
    
    autotools.autoreconf("-fi")
    autotools.configure("--libdir=/usr/lib \
                         --enable-nls \
                         --disable-audit \
                         --enable-securedir=/lib/security \
                         --enable-isadir=/lib/security")
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    # Update .po files
    autotools.make("-C po update-gmo")

    autotools.make()

def check():
    autotools.make("check")

    # dlopen check
    shelltools.system("./dlopen-test.sh")
    pass

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.removeDir("/usr/share/doc/Linux-PAM/")

    inarytools.doman("doc/man/*.[0-9]")
    inarytools.dodoc("CHANGELOG", "Copyright", "README")

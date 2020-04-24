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
    autotools.configure("--libdir=/usr/lib{0} \
                         --enable-nls \
                         --disable-audit \
                         --enable-securedir=/lib{0}/security \
                         --enable-isadir='.'".format("32" if get.buildTYPE()=="emul32" else ""))

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
    if get.buildTYPE()=="emul32":
        return

    inarytools.removeDir("/usr/share/doc/Linux-PAM/")

    inarytools.doman("doc/man/*.[0-9]")
    inarytools.dodoc("CHANGELOG", "Copyright", "README")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import libtools
from inary.actionsapi import get

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc/gpm \
                         --sbindir=/usr/bin")
                         #--libdir=/usr/lib \

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove this when we can break abi
    inarytools.dosym("libgpm.so.2", "/usr/lib/libgpm.so")

    #remove static link
    inarytools.remove("/usr/lib/libgpm.a")

    inarytools.insinto("/etc/gpm", "conf/gpm-*.conf")

    inarytools.dodoc("COPYING", "README", "TODO", "doc/Announce", "doc/FAQ", "doc/README*")

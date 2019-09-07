#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    autotools.configure("--sysconfdir=/etc \
                         --with-zlib \
                         --with-xz")

def build():
    autotools.make()

# need git for check
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32": return

    inarytools.dosym("modprobe.d.5","/usr/share/man/man5/modprobe.conf.5")
    for sym in ["modinfo","insmod","rmmod","depmod","modprobe"]:
        inarytools.dosym("../usr/bin/kmod","/sbin/%s" % sym)
    inarytools.dosym("../usr/bin/kmod","/bin/lsmod")
    inarytools.makedirs("%s/etc/depmod.d" % get.installDIR())
    inarytools.makedirs("%s/etc/modprobe.d" % get.installDIR())
    inarytools.dodoc("NEWS", "README", "TODO", "COPYING")

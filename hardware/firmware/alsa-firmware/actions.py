#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

NoStrip = ["/"]


def setup():
    autotools.configure("--with-hotplug-dir=/lib/firmware")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #Remove conflicted file, it is in linux-firmware package
    inarytools.remove("lib/firmware/ctefx.bin")
    inarytools.remove("lib/firmware/ctspeq.bin")

    # Install additional readme files
    for d in ["hdsploader", "mixartloader", "pcxhrloader", "usx2yloader", "vxloader"]:
        inarytools.newdoc("%s/README" % d, "README.%s" % d)

    inarytools.dodoc("COPYING", "README")

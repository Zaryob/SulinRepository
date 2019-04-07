#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import kerneltools

KDIR = kerneltools.getKernelVersion()

def build():
    autotools.make("KDIR=/lib/modules/%s/build" % KDIR)
    #autotools.make()

def install():
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.insinto("/lib/modules/%s/misc" % KDIR, "bbswitch.ko")

    inarytools.dodoc("NEWS", "README*")

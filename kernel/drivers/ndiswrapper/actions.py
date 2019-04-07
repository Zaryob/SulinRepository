#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import kerneltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

KDIR = kerneltools.getKernelVersion()

def build():
    autotools.make("-C driver KVERS_UNAME=%s" % KDIR)

    autotools.make("-C utils")

def install():
    inarytools.insinto("/lib/modules/%s/extra" % KDIR, "*/*.ko")
    inarytools.dosbin("utils/ndiswrapper*", "/usr/sbin")
    inarytools.dosbin("utils/loadndisdriver", "/sbin")
    
    # add man
    inarytools.doman("*.8")
    
    inarytools.dodir("/etc/ndiswrapper")

    inarytools.dodoc("README", "AUTHORS", "ChangeLog")

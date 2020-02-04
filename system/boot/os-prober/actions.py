#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def build():
    #shelltools.unlink("Makefile")
    autotools.make()
    autotools.make("newns")

def install():
    inarytools.dodoc("debian/copyright", "debian/changelog", "README")
    inarytools.dobin("os-prober")
    inarytools.dobin("linux-boot-prober")
    inarytools.insinto("/usr/lib/os-prober", "newns")
    inarytools.insinto("/usr/share/os-prober", "common.sh")
    for d in ("os-probes",
              "os-probes/mounted", 
              "os-probes/init",
              "linux-boot-probes",
              "linux-boot-probes/mounted"):
        inarytools.insinto("/usr/lib/%s" % d, "%s/common/*" % d)
        if shelltools.isDirectory("%s/x86" % d):
            inarytools.insinto("/usr/lib/%s" % d, "%s/x86/*" % d)
    shelltools.touch("labels")
    inarytools.insinto("/var/lib/os-prober/", "labels")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Suleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def build():
    shelltools.export("GOPATH", "%s" % get.workDIR())

    shelltools.cd("%s" % get.workDIR())
    shelltools.move("containerd-*", "containerd")

    shelltools.cd("containerd")
    shelltools.move("vendor", "src")

    shelltools.makedirs("src/github.com/containerd")
    shelltools.system("ln -rsf %s/containerd*  src/github.com/containerd" % get.workDIR())

    shelltools.cd("src/github.com/containerd/containerd")

    shelltools.system("LDFLAGS= GOPATH=%s make GIT_COMMIT=209a7fc" % get.curDIR())

def install():
    shelltools.cd("%s/containerd" % get.workDIR())

    inarytools.dobin("bin/*")

    inarytools.dosym("/usr/bin/containerd", "/usr/bin/docker-containerd")
    inarytools.dosym("/usr/bin/containerd-shim", "/usr/bin/docker-containerd-shim")
    inarytools.dosym("/usr/bin/ctr", "/usr/bin/docker-containerd-ctr")

    inarytools.dodoc("LICENSE*", "README*")

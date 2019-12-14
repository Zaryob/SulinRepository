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

shelltools.export("DOCKER_BUILDTAGS","seccomp apparmor")
shelltools.export("BINDIR","/usr/bin")

def setup():
    shelltools.cd("%s" % get.workDIR())
    shelltools.move("runc-*", "runc")

    shelltools.cd("runc")
    shelltools.move("vendor", "src")

    shelltools.makedirs("src/github.com/opencontainers")
    shelltools.cd("src/github.com/opencontainers")

    shelltools.system("ln -rsf %s/runc ./runc" % get.workDIR())

def build():
    shelltools.cd("%s/runc/src/github.com/opencontainers/runc" % get.workDIR())

    build_runc = "GOPATH=%s/runc make" % get.workDIR()

    shelltools.system(build_runc)

def install():
    inarytools.dobin("runc")

    inarytools.dosym("/usr/bin/runc", "/usr/bin/docker-runc")

    inarytools.insinto("/usr/share/doc/runc", "contrib")

    inarytools.dodoc("MAINTAINERS", "README*")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import get

shelltools.export("AUTO_GOPATH", "1")
shelltools.export("IAMSTATIC", "false")
shelltools.export("DOCKER_GITCOMMIT","633a0ea")
shelltools.export("VERSION", "19.03.5")
shelltools.export("GOROOT","/usr/lib/go")

shelltools.export("GOPATH", "%s" % get.workDIR())
shelltools.export("CGO_CFLAGS", "-I/usr/include")
shelltools.export("CGO_LDFLAGS", "-L/usr/lib")
shelltools.export("DOCKER_BUILDTAGS","apparmor seccomp")

NoStrip=["/"]

def setup():
    shelltools.makedirs("components/cli/src/github.com/docker")
    shelltools.cd("components/cli/src/github.com/docker")
    shelltools.system("ln -s ../../../../cli . ")

def build():
    shelltools.cd("%s" % get.workDIR())
    shelltools.cd("docker-ce-%s/components/engine" % get.srcVERSION())
    shelltools.system("hack/make.sh dynbinary-daemon")

    # build cli
    shelltools.cd("%s" % get.workDIR())
    shelltools.cd("docker-ce-%s/components/cli" % get.srcVERSION())
    shelltools.system("LDFLAGS='' GOPATH=%s/docker-ce-%s/components/cli ./scripts/build/dynbinary" % (get.workDIR(), get.srcVERSION()))

def install():
    shelltools.cd("%s/docker-ce-%s" % (get.workDIR(), get.srcVERSION()))

    inarytools.dobin("components/cli/build/docker*")
    inarytools.dobin("components/engine/bundles/dynbinary-daemon/*")

    # insert udev rules
    inarytools.insinto("/lib/udev/rules.d", "components/engine/contrib/udev/*.rules")

    #insert contrib in docs
    inarytools.insinto("/usr/share/doc/docker", "components/cli/contrib")

    inarytools.dobin("components/engine/contrib/check-config.sh")

    inarytools.dodoc("VERSION", "README.md","CONTRIBUTING.md", "CHANGELOG.md")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import get

NoStrip = ["/"]
#NoStrip = ["/usr/lib/go/pkg", "/usr/lib/go/src/runtime/race", "/usr/lib/go/src/debug/elf", "/usr/lib/go/src/debug/dwarf"]

shelltools.export("go_platform","linux-amd64")
shelltools.export("go_linker","/lib/ld-linux-x86-64.so.2")

shelltools.export("GOROOT", "%s/go-go1.13.4" % get.workDIR()) #0

shelltools.export("GOBIN", "$GOROOT/bin") #1
shelltools.export("GOPATH", "%s" % get.workDIR())
shelltools.export("GOROOT_FINAL", "/usr/lib/go")
shelltools.export("GOROOT_BOOTSTRAP", "%s/go-go1.13.4/go-linux-amd64-bootstrap" % get.workDIR())  #2

shelltools.export("GOOS","linux")
shelltools.export("GOARCH","amd64")

def setup():

    shelltools.cd("src")

    shelltools.system("./make.bash")

    shelltools.cd("%s/go-go1.13.4" % get.workDIR())
    shelltools.system("$GOROOT/bin/go get -d golang.org/x/tools/cmd/godoc")
    shelltools.system("$GOROOT/bin/go build -o $GOPATH/godoc golang.org/x/tools/cmd/godoc")

def build():
    for tool in ["godex", "godoc", "goimports", "gomvpkg",
    "gorename", "gotype", "goyacc", "auth/authtest",
    "auth/cookieauth", "auth/gitauth", "auth/netrcauth",
    "benchcmp", "bundle", "callgraph", "compilebench",
    "cover", "digraph", "eg", "fiximports", "getgo",
    "go-contrib-init", "gopls", "guru", "html2article",
    "splitdwarf", "present", "ssadump", "stress", "stringer",
    "toolstash"]:
        shelltools.system("$GOROOT/bin/go get -d golang.org/x/tools/cmd/%s" % tool)
        shelltools.system("$GOROOT/bin/go build -v -x -o $GOROOT/pkg/tool/$GOOS\_$GOARCH/%s golang.org/x/tools/cmd/%s" % (tool, tool))


def install():
    shelltools.export("GOROOT_FINAL", "/usr/lib/go")
    shelltools.cd("%s/go-go1.13.4" % get.workDIR())

    inarytools.dodir("/usr/lib/go")
    shelltools.system("cp -r api bin doc lib pkg src  %s/usr/lib/go" % get.installDIR())
    shelltools.system("chown -R  root:root %s/usr" % get.installDIR())

    inarytools.dosym("/usr/lib/go/bin/go", "/usr/bin/go")
    inarytools.dosym("/usr/lib/go/bin/gofmt", "/usr/bin/gofmt")

    inarytools.dosym("/usr/lib/go/doc", "/usr/share/doc/%s/doc" % get.srcNAME())
    inarytools.dosym("/usr/lib/go/api", "/usr/share/doc/%s/api" % get.srcNAME())

    shelltools.system("cp -r misc  %s/usr/lib/go" % get.installDIR())

    # remove testdata, which hit cave fix-linkage
    inarytools.remove("/usr/lib/go/src/debug/elf/testdata/gcc-386-freebsd-exec")
    inarytools.removeDir("/usr/lib/go/pkg/obj")

    # dirty fix thanks @erturk
    inarytools.removeDir("/usr/lib/go/pkg/linux_amd64")


    inarytools.dodoc("VERSION", "LICENSE", "PATENTS", "README*", "AUTHORS", "CONTRIBUTORS")

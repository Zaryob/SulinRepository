# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

WorkDir = "."
SkipList = (".", "filelist", "patches", "inaryBuildState", "tmp")


def setup():
    # Speed up xkbcomp
    shelltools.export("CFLAGS","%s -DHAVE_STRCASECMP" % get.CFLAGS())

    for package in shelltools.ls("."):
        if package.startswith(SkipList):
            continue

        print ("\nConfiguring %s..." % package)
        print ("-" * (len(package) + 15))
        shelltools.cd(package)

        if package.startswith(("xcursorgen", "xsm")) or \
                not shelltools.isFile("configure"):
            autotools.autoreconf("-vif")
        elif package.startswith("luit"):
            inarytools.dosed("configure.ac", "(-D_XOPEN_SOURCE)=500", "\\1=600")
            autotools.autoreconf("-vif")

        autotools.configure("--disable-dependency-tracking \
                             --disable-devel-docs \
                             --with-cpp=/usr/bin/mcpp")
        shelltools.cd("../")

def build():
    for package in shelltools.ls("."):
        if package.startswith(SkipList):
            continue

        shelltools.cd(package)
        if package.startswith("xfwp"): inarytools.dosed("io.c", "^(#include <unistd.h>)", r"#define __USE_XOPEN\n\1")
        autotools.make()
        shelltools.cd("../")

def install():
    for package in shelltools.ls("."):
        if package.startswith(SkipList):
            continue

        shelltools.cd(package)
        autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("../")

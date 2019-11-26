#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    shelltools.export("OPTIMIZER", "%s" % get.CFLAGS())
    shelltools.export("DEBUG", "-DNDEBUG")

    autotools.configure("--enable-readline=yes \
                         --enable-blkid=yes")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DIST_ROOT=%s" % get.installDIR())
    autotools.rawInstall("DIST_ROOT=%s" % get.installDIR(), "install-dev")
    # Needed for building the QA testsuite
    #autotools.rawInstall("DIST_ROOT=%s" % get.installDIR(), "install-qa")

    # Nuke static libraries
    #inarytools.remove("/lib/libhandle.a")
    #inarytools.remove("/lib/libhandle.la")
    #inarytools.remove("/usr/lib/*.a")

    # Fix the symlink
    #inarytools.remove("/usr/lib/libhandle.so")
    #inarytools.dosym("/lib/libhandle.so.1", "/usr/lib/libhandle.so")

    # Set +x bit for the library
    shelltools.chmod("%s/lib/libhandle.so.*.*.*" % get.installDIR(), 0o755)

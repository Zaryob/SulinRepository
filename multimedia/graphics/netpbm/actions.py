#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/copy-left/gpl-3.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get
import os


def makedepends(d):
    for root, dirs, files in os.walk(d):
        for name in files:
            if name == "Makefile":
                shelltools.touch(os.path.join(root, "depend.mk"))

def setup():
    inarytools.dosed("config.mk", "^STRIPFLAG.*=.*", "STRIPFLAG = ")

    # force external jasper usage
    inarytools.echo("config.mk", "JASPERLIB = -ljasper")
    inarytools.echo("config.mk", "JASPERHDR_DIR = /usr/include/jasper")

    makedepends("./")

def build():
    autotools.make('CFLAGS="%s -fPIC -O3 -ffast-math -pedantic -fno-common" LDFLAGS="%s" -j1' % (get.CFLAGS(), get.LDFLAGS()))

def install():
    inarytools.dodir("/")
    autotools.make('-j1 package pkgdir=%s/usr' % get.installDIR())

    inarytools.remove("/usr/bin/manweb")

    for data in ["VERSION","pkginfo","README","pkgconfig_template","config_template"]:
        inarytools.remove("/usr/%s" % data)

    for directory in ["link", "man/web"]:
        inarytools.removeDir("/usr/%s" % directory)

    inarytools.domove("/usr/misc", "/usr/share/netpbm")
    inarytools.domove("/usr/man", "/usr/share")

    # remove conflicts with jbigkit
    for i in ["pbm", "pgm"]:
        inarytools.remove("/usr/share/man/man5/%s.5" % i)

    inarytools.dodoc("README", "doc/*LICENSE*")

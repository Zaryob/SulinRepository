#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.unlink("m4/glib-gettext.m4")
    shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr \
                         --disable-static \
                         --enable-cli \
                         --disable-daemon")


def build():
    autotools.make()


def install():

    # gtk
    autotools.rawInstall("-C gtk DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C po DESTDIR=%s" % get.installDIR())

    # cli,web, deamon
    for _dir in ["cli", "web", "utils"]:
        autotools.rawInstall("-C %s DESTDIR=%s" % (_dir, get.installDIR()))

    # For daemon config files.
    inarytools.dodir("/etc/transmission-daemon")

    inarytools.dodoc("COPYING", "AUTHORS", "README", "NEWS")

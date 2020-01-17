#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import libtools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    # Use system libtool instead of bundled one
    shelltools.unlinkDir("libltdl")
    libtools.libtoolize("-c -f --ltdl")
    autotools.autoreconf("-fi")

    autotools.configure("--sysconfdir=/etc/unixODBC \
                         --disable-dependency-tracking \
                         --disable-gui \
                         --enable-threads \
                         --enable-drivers \
                         --enable-driver-conf \
                         --disable-stats ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
    inarytools.dohtml("doc/*")

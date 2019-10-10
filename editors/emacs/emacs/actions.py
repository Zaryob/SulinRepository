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
    #autotools.autoreconf("-fvi")
    autotools.configure("--with-x-toolkit=gtk \
                         --with-xft \
                         --with-modules")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.removeDir("/usr/lib/systemd") # No systemd
    inarytools.removeDir("/usr/lib") # No empty dir

    inarytools.dodoc("ChangeLog", "BUGS", "README", "COPYING")

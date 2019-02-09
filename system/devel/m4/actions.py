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
#    shelltools.system("sed -i -e '/gets is a/d' lib/stdio.in.h")
    autotools.autoreconf("-vif")
    autotools.configure("--enable-nls \
                         --enable-changeword")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("BACKLOG", "ChangeLog", "NEWS", "README*", "THANKS", "TODO")

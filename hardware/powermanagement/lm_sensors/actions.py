#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    autotools.make("PREFIX=/usr")

def install():
    autotools.rawInstall("PREFIX=/usr BUILD_STATIC_LIB=0 MANDIR=/%s PROG_EXTRA=sensord DESTDIR=%s user_install" % (get.manDIR(), get.installDIR()))

    inarytools.dodoc("CHANGES", "CONTRIBUTORS", "README")

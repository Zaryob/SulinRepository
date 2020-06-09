#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Suleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--enable-linux-multiformat")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR={}".format(get.installDIR()))

    inarytools.dodir("/var/account")

    inarytools.remove("/usr/bin/last")
    inarytools.remove("/usr/share/man/man1/last.1")

    inarytools.dodoc("AUTHORS", "ChangeLog", "TODO", "COPYING", "NEWS", "README")
    inarytools.dodir("/sbin")
    inarytools.move("{}/usr/sbin/accton".format(get.installDIR()),"{}/sbin/".format(get.installDIR()))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    autotools.make()

def install():
    #rename netcat binary to differentiate it from gnu version
    inarytools.insinto("/usr/bin/", "nc", "netcat-openbsd")
    #insert a symlink as nc so that applications expecting nc command can run it
    inarytools.dosym("./netcat-openbsd", "/usr/bin/nc")

    # copy the man stuff and create a symlink for both command possibilities
    inarytools.doman("nc.1")
    inarytools.dosym("./nc.1", "/usr/share/man/man1/netcat-openbsd.1")

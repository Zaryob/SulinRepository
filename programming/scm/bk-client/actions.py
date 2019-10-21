#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Suleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 3.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

NoStrip="/"
WorkDir="."

def setup():
    shelltools.chmod("bk-7.3.2-x86_64-glibc27-linux.bin", 0o755)

def install():
    shelltools.system("./bk-7.3.2-x86_64-glibc27-linux.bin {}/opt/bitkeeper".format(get.installDIR()))
    inarytools.dodir("/usr/bin")
    inarytools.dosym("/opt/bitkeeper/bk", "/usr/bin/bk")
    inarytools.domove("/opt/bitkeeper/man", "/usr/share/")
    inarytools.domove("/usr/share/man/man1/patch.1", "/usr/share/man/man1/bk_patch.1")

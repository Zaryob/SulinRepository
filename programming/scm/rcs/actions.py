#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Suleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import inarytools
from inary.actionsapi import autotools
from inary.actionsapi import get

InstDir = get.installDIR()
manDir = get.manDIR()


def setup():
    autotools.rawConfigure("--with-diffutils \
                            --prefix=/%s \
                            --host=%s \ " %
                            (get.defaultprefixDIR(), \
                             get.HOST()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("prefix=%s/usr \
                          man1dir=%s/%s/man1 \
                          man3dir=%s/%s/man3 \
                          man5dir=%s/%s/man5" %
                          (InstDir,InstDir,manDir,InstDir,
                          manDir,InstDir,manDir))
    inarytools.dodoc("ChangeLog", "CREDITS", "NEWS", "README", "REFS")

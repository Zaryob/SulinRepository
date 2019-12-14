#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    #shelltools.export("DEFS", "NO_ASM")
    autotools.configure("--exec-prefix=/")

def build():
    autotools.make()

def check():
    pass
    # check fail, need util-linux, in dockerized build check disabled. install util-linux and make check
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # add missing gzcat
    inarytools.dosym("zcat", "/bin/gzcat")

    inarytools.dodoc("ChangeLog", "NEWS", "README", "THANKS", "TODO")

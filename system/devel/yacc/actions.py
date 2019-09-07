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
    shelltools.system("tar xvf yacc-1.9.1.tar.Z")
    shelltools.cd("{}/yacc-1.9.1".format(get.workDIR()))
    for i in ["mkstemp.patch", "skeleton.c.diff", "yacc-1.9.1-ia64.patch"]:
        shelltools.move("../{}".format(i), ".")
        shelltools.system("patch --remove-empty-files --no-backup-if-mismatch -i \"{}\"".format(i))
    inarytools.dosed("Makefile", " -O ", " $(CFLAGS) ")

def build():
    shelltools.cd("{}/yacc-1.9.1".format(get.workDIR()))

    autotools.make("clean")
    autotools.make('-j1 CC="%s" CFLAGS="%s"' % (get.CC(), get.CFLAGS()))

def install():
    shelltools.cd("{}/yacc-1.9.1".format(get.workDIR()))

    inarytools.dobin("yacc")

    inarytools.doman("yacc.1")
    inarytools.dodoc("ACKNOWLEDGEMENTS", "NEW_FEATURES", "NOTES", "README*")

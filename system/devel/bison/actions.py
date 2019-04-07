#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def check():
    #autotools.make("check")
    pass

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.rename("/usr/bin/yacc", "yacc.bison")
    inarytools.rename("/usr/share/man/man1/yacc.1", "yacc.bison.1")

    #inarytools.removeDir("/usr/lib/")

    inarytools.dodoc("AUTHORS", "NEWS", "ChangeLog", "README", "COPYING")

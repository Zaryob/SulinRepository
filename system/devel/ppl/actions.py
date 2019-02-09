#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get


def setup():
    autotools.configure('--enable-interfaces="c,cxx"')
def build():
    autotools.make()

# tests run hours and hours, running it is left to packager
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("BUGS", "COPYING", "CREDITS", "ChangeLog", "STANDARDS", "TODO", "README*", "NEWS")

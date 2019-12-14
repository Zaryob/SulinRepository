#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
WorkDir = "feh-3.2.1"

#def setup():

def build():
    autotools.make("PREFIX=/usr")
def install():
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s" % get.installDIR())
    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "TODO")

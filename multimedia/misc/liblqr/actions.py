#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "%s-1-%s" % (get.srcNAME(), get.srcVERSION())

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.removeDir("/usr/share/man")

    inarytools.dodoc("AUTHORS", "COPYING*", "ChangeLog", "README", "NEWS")

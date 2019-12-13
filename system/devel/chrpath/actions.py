#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("docdir=/usr/share/doc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.removeDir("/usr/doc")
    inarytools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README" ,"COPYING")


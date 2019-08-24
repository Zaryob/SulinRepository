#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import get
from inary.actionsapi import inarytools



def setup():
    autotools.configure("--prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.domove("/usr/share/autoconf-archive/", "/usr/share/doc")
    inarytools.dodoc("AUTHORS", "NEWS", "ChangeLog", "COPYING", "README")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr --disable-appindicator")

def build():
    autotools.make("DESTDIR={}".format(get.installDIR()))

def install():
    autotools.install()

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

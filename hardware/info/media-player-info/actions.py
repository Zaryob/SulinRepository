#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    # force to use python2.x
    #inarytools.dosed("configure.ac", "(python)3", "\\1")

    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr \
                         --with-udevdir=/lib/udev")

def build():
    autotools.make('LANG="en_US.UTF-8"')

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS")

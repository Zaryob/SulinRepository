#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import get
from inary.actionsapi import inarytools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #remove after usbmove
    inarytools.dosym("/usr/sbin/biosdevname", "/sbin/biosdevname")

    inarytools.dodoc("AUTHORS", "NEWS", "ChangeLog", "COPYING", "TODO", "README")

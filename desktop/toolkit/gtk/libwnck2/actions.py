#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    #autotools.autoreconf("-vif")
    autotools.configure("--disable-static --enable-introspection")

    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.rename("/usr/bin/wnckprop", "wnckprop")
    inarytools.rename("/usr/bin/wnck-urgency-monitor", "wnck-urgency-monitor2")

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "MAINTAINERS")

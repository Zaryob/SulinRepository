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

    inarytools.remove("/usr/bin/wnck-urgency-monitor")
    inarytools.remove("/usr/bin/wnckprop")
    
    inarytools.removeDir("/usr/share/gtk-doc")
    inarytools.removeDir("/usr/bin")

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "MAINTAINERS")

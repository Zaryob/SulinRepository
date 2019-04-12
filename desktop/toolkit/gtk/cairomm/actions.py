#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure("--disable-static")
    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.removeDir("/usr/share/devhelp")

    #move html docs to html doc dir
    inarytools.dodir("/usr/share/doc/%s/html" % get.srcNAME())
    inarytools.domove("/usr/share/doc/%s-1.0/*" % get.srcNAME(), "/usr/share/doc/%s/html" % get.srcNAME())
    inarytools.removeDir("/usr/share/doc/%s-1.0" % get.srcNAME())

    inarytools.dodoc("AUTHORS", "README", "COPYING", "ChangeLog", "NEWS")

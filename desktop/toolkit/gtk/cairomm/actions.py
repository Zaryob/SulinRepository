#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    autotools.configure("CC=\"{} -std=c++17\" CXX=\"{} -std=c++17\" --disable-static".format(get.CC(),get.CXX()))
    inarytools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR={}".format(get.installDIR()))

    inarytools.removeDir("/usr/share/devhelp")

    #move html docs to html doc dir
    inarytools.dodir("/usr/share/doc/{}/html".format(get.srcNAME()))
    inarytools.domove("/usr/share/doc/{}-1.0/*".format(get.srcNAME()), "/usr/share/doc/{}/html".format(get.srcNAME()))
    inarytools.removeDir("/usr/share/doc/{}-1.0".format(get.srcNAME()))

    inarytools.dodoc("AUTHORS", "README", "COPYING", "ChangeLog", "NEWS")

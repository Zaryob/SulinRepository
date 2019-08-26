#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

#ver = "1.14"

def setup():
    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    autotools.make()

#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Use gnuconfig files
#    for config in ["config.guess","config.sub"]:
#        inarytools.remove("/usr/share/automake-%s/%s" % (ver, config))
#        inarytools.dosym("/usr/share/gnuconfig/%s" % config, "/usr/share/automake-%s/%s" % (ver, config))

    inarytools.dodoc("NEWS", "README", "THANKS","AUTHORS", "ChangeLog*")

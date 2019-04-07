#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

configTemplateDir = "/usr/share/libtool/config"

def setup():
    #inarytools.cflags.add("-fPIC")
    #autotools.configure("--enable-static=no")
    autotools.configure()


def build():
    autotools.make()

def check():
    pass
    # test failed in dockerized build. 
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #for f in ["config.sub", "config.guess"]:
        #inarytools.remove("%s/%s" % (configTemplateDir, f))
        #inarytools.dosym("/usr/share/gnuconfig/%s" % f, "%s/%s" % (configTemplateDir, f))

    inarytools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "NEWS", "README", "THANKS", "doc/PLATFORMS")


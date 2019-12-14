#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

import os
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

WorkDir="Firebird-%s-0" % get.srcVERSION()

def setup():
    autotools.configure("--prefix=/usr \
                         --with-fbbin=/usr/bin \
                         --with-fbconf=/etc/firebird \
                         --with-fbdoc=/usr/share/doc/firebird \
                         --with-fbglock=/run/firebird \
                         --with-fbhelp=/usr/share/doc/firebird/help \
                         --with-fbinclude=/usr/include/firebird \
                         --with-fblib=/usr/lib \
                         --with-fblog=/var/log/ \
                         --with-fbmsg=/usr/lib/firebird/msg \
                         --with-fbplugins=/usr/lib/firebird/plugins \
                         --with-fbsbin=/usr/lib/firebird/bin \
                         --with-fbudf=/usr/lib/firebird/UDF \
                         --with-fbsecure-db=/var/lib/firebird/system \
                         --with-fbintl=/usr/lib/firebird/intl \
                         --without-fbmisc \
                         --without-fbsample \
                         --without-fbsample-db \
                         --enable-superserver \
                         --with-system-icu \
                         --with-system-editline \
                         ")

def build():
    #Parallel build is broken
    shelltools.export("CXXFLAGS", "%s -std=gnu++98 -fno-lifetime-dse" % get.CXXFLAGS())
    autotools.make()
    shelltools.cd("gen")
    inarytools.dosed("install/makeInstallImage.sh", "exit 1", "# exit 1")
    inarytools.dosed("install/makeInstallImage.sh", "chown", 'echo ""# chown')
    inarytools.dosed("install/makeInstallImage.sh", "chmod", 'echo ""# chmod')
    autotools.make("-f Makefile.install buildRoot")

def install():
    # Copy to install directory
    shelltools.copytree("gen/buildroot/", get.installDIR())
    inarytools.domove("/usr/bin/isql", "/usr/bin/isql-firebird")

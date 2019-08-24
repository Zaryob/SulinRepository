#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import libtools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--enable-jit \
                         --enable-pcretest-libreadline \
                         --enable-pcre32 \
                         --enable-pcre16 \
                         --enable-utf \
                         --enable-unicode-properties \
                         --enable-cpp \
                         --docdir=/%s/%s \
                         --disable-static" % (get.docDIR(), get.srcNAME()))
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def check():
    if get.buildTYPE() == "emul32":
        pass
    else:
        autotools.make("-j1 check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

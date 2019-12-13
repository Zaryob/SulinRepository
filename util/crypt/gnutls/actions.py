#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    options = "--disable-static \
               --disable-rpath \
               --disable-silent-rules \
               --disable-guile \
               --enable-heartbeat-support \
               --with-zlib \
               --without-tpm \
               --without-dane \
               --disable-valgrind-tests"

    if get.buildTYPE() == "emul32":
        options += " --disable-hardware-acceleration \
                    --with-included-unistring \
                     --enable-local-libopts \
                   "

    autotools.configure(options)

    inarytools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

#def check():
    #some tests fail in emul32
    #if not get.buildTYPE() == "emul32":
        #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

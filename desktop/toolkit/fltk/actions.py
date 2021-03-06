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
    inarytools.flags.add("-fPIC")
    inarytools.dosed("makeinclude.in", "^(docdir.*)$", r"\1/html")

    autotools.autoconf()

    options = "\
               --enable-gl \
               --enable-shared \
               --enable-threads \
               "

    if get.buildTYPE() == "emul32":

        shelltools.export("CFLAGS", "-m32")
        shelltools.export("CXXFLAGS", "-m32")

        options += "--prefix=/emul32 \
                    --libdir=/usr/lib32 \
                    --with-optim='%s' \
                    " % get.CFLAGS()

    elif get.ARCH() == "x86_64":

        options += "--with-optim='%s' \
                   "  % get.CFLAGS()

    autotools.configure(options)

def build():
    autotools.make()
    autotools.make("-C documentation all")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    autotools.rawInstall("DESTDIR=%s -C fluid " % get.installDIR(), " install-linux")
    
    if get.buildTYPE() == "emul32": return
    
    autotools.install("-C documentation")
    inarytools.dodoc("ANNOUNCEMENT", "CHANGES", "COPYING", "CREDITS", "README")

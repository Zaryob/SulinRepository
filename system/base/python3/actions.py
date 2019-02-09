#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    inarytools.flags.add("-fwrapv")

    inarytools.dosed("Lib/cgi.py","^#.* /usr/local/bin/python","#!/usr/bin/env python3")

    autotools.rawConfigure("\
                            --prefix=/usr \
                            --enable-shared \
                            --with-threads \
                            --with-computed-gotos \
                            --enable-ipv6 \
                            --with-system-expat \
                            --with-dbmliborder=gdbm:ndbm \
                            --with-system-ffi \
                            --with-system-libmpdec \
                            --enable-loadable-sqlite-extensions \
                            --without-ensurepip")

def build():
    autotools.make()

#def check():
#    autotools.make('test')

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.remove("/usr/bin/2to3")
    inarytools.dodoc("LICENSE", "README*")

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
    #shelltools.copy("makefiles/configure.in", "configure.in")
    shelltools.copy("makefiles/Makefile.am", "Makefile.am")
    shelltools.copy("makefiles/makefile.linux", "Makefile")
    #shelltools.sym("contrib/gcc/sdl-mngplay/acinclude.m4", "acinclude.m4")
    
    shelltools.system("sed -i -e 's/unroll-loops/& -fPIC/' Makefile ")

    autotools.autoreconf("-fiv")
    autotools.configure("--with-jpeg \
                         --with-lcms \
                         --disable-static \
                         --disable-dependency-tracking")

    if get.buildTYPE() == "emul32":
        options = " --libdir=/usr/lib32 \
                    --with-jpeg \
                    --disable-static \
                    --disable-dependency-tracking"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.doman("doc/man/*")
    inarytools.dodoc("CHANGES", "LICENSE", "README*", "doc/doc.readme", "doc/misc/*", "doc/libmng.txt")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    # use python2.x
    inarytools.dosed("configure", "(\/usr\/include\/)python\*", r"\1python2*")
    # fix unused direct dependency
    inarytools.dosed("Makefile.in", "(PLFLAGS=)`\$\$pyconfig --libs`", r"\1'-lpython2.7'")
    inarytools.dosed("Makefile.in", "(PLDFLAGS=)`\$\$pyconfig --ldflags`", r"\1'-lpython2.7 -Xlinker -export-dynamic'")

    shelltools.echo("config.h.in", "#define USE_INTERP_RESULT 1")
    shelltools.export("PYTHON", "/usr/bin/python2.7")
    autotools.configure("\
                         --with-gpm-support \
                        ")

def build():
    autotools.make()

def install():
    autotools.install()

    # remove static lib
    inarytools.remove("/usr/lib/libnewt.a")

    inarytools.dodoc("CHANGES", "COPYING")

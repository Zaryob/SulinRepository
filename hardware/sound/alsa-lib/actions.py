#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools

def setup():
    options = "--disable-aload"

    if get.buildTYPE() == "emul32":
        options += " --disable-python"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
    else:
        options += " --enable-python \
                    --with-python=/usr/bin/python3"
        shelltools.export("PYTHON", "/usr/bin/python3")

    autotools.configure(options)
    inarytools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

    # rpath fix
    inarytools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    inarytools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32": return

    inarytools.dodoc("ChangeLog", "TODO", "COPYING", "doc/*.txt")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    python = "--without-python" if get.buildTYPE() == "emul32" else "--with-python=/usr/bin/python3.7 "
    # don't remove --with-debugger as it is needed for reverse dependencies
    autotools.configure("%s \
                         --with-crypto \
                         --with-debugger \
                         --disable-static \
                         --with-xz \
                         --with-zlib \
                         --disable-silent-rules \
                        " % python)

    inarytools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    inarytools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("AUTHORS", "ChangeLog", "Copyright", "FEATURES", "NEWS", "README", "TODO")

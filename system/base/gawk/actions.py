#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    shelltools.export("ac_cv_libsigsegv", "no")
    shelltools.export("AUTOPOINT", "true")
    autotools.configure("--with-libsigsegv-prefix=no \
                         --enable-switch \
                         --enable-nls")

def build():
    autotools.make()

#def check():
#    autotools.make("-j1 check diffout")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove versioned binaries
    inarytools.remove("/usr/bin/*-%s" % get.srcVERSION())

    inarytools.dosym("gawk.1", "/usr/share/man/man1/awk.1")
    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

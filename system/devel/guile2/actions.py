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
    autotools.autoreconf("-vif")
    autotools.configure("--disable-error-on-warning \
                         --disable-static \
                         --enable-posix \
                         --enable-networking \
                         --enable-regex \
                         --enable-nls \
                         --disable-rpath \
                         --with-threads \
                         --with-modules")
    
    inarytools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

    # Put flags in front of the libs. Needed for --as-needed.
    replace = (r"(\\\$deplibs) (\\\$compiler_flags)", r"\2 \1")
    #inarytools.dosed("libtool", *replace)
    #inarytools.dosed("*/libtool", *replace)

def build():
    autotools.make()

def install():
    autotools.install()
    inarytools.removeDir("/usr/share/info")
    inarytools.removeDir("/usr/share/man")
    inarytools.removeDir("/usr/share/aclocal")
    inarytools.remove("/usr/bin/guild")
    inarytools.remove("/usr/bin/guile")
    inarytools.remove("/usr/bin/guile-tools")
    inarytools.remove("/usr/bin/guile-config")
    inarytools.remove("/usr/bin/guile-snarf")
    major = ".".join(get.srcVERSION().split(".")[:2])
    
    inarytools.dodoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", "README", "THANKS")

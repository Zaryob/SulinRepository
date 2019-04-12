#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    shelltools.system('sed -i -e "/AC_PATH_XTRA/d" configure.in')
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static")

    # Put flags in front of the libs. Needed for --as-needed.
    replace = (r"(\\\$deplibs) (\\\$compiler_flags)", r"\2 \1")
    inarytools.dosed("libtool", *replace)

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "doc/startup-notification.txt")
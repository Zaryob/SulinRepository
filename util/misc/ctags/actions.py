#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.configure("--with-posix-regex \
                         --without-readlib \
                         --disable-etags \
                         --enable-tmpdir=/tmp")

def build():
    autotools.make()

def install():
    autotools.install()

    # Don't conflict with emacs
    inarytools.rename("/usr/bin/ctags", "exuberant-ctags")
    inarytools.rename("/usr/share/man/man1/ctags.1", "exuberant-ctags.1")

    inarytools.dohtml("EXTENDING.html", "ctags.html")
    inarytools.dodoc("COPYING", "FAQ", "NEWS", "README")

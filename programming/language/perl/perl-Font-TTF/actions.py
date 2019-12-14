#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import perlmodules
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import autotools
from inary.actionsapi import get

WorkDir="Font-TTF-%s" % get.srcVERSION()

def setup():
    for d in ("README.TXT", "TODO", "Changes"):
        shelltools.chmod(d, 0o644)

    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    inarytools.dodoc("README*", "TODO", "Changes")

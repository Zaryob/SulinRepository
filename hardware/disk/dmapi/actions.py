#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import libtools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    autotools.configure("--libexecdir=/usr/lib \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DIST_ROOT="%s" install-dev' % get.installDIR())

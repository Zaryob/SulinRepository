#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import shelltools


def build():
    autotools.make()

def install():
    inarytools.dodir("/usr/bin")
    shelltools.system("install tinywm {}/usr/bin/tinywm".format(get.installDIR()))

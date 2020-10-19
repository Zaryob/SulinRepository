#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import get
from inary.actionsapi import inarytools

def build():
    autotools.make()

def install():
    shelltools.system("mkdir -p {}/bin/".format(get.installDIR()))
    autotools.install("DESTDIR={0} DSDIR={0}/usr/share/debootstrap/".format(get.installDIR()))
    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import autotools
from inary.actionsapi import get
from inary.actionsapi import variables
import os
def build():
     autotools.make("-C lib PREFIX=/usr")
     autotools.make("-C programs lz4 lz4c PREFIX=/usr")

def install():
    # TODO: we must use autotools
    backup_environ=os.environ.copy()
    pkgdir=get.installDIR()
    os.environ.clear()
    os.environ["PATH"]="/bin:/usr/bin:/sbin:/usr/sbin"
    os.system('make install Q=" " -C lib PREFIX=/usr PREFIX=/usr DESTDIR='+pkgdir)
    os.system('make install Q=" " -C programs PREFIX=/usr DESTDIR='+pkgdir)
    os.environ.update(backup_environ)

    inarytools.dodoc("LICENSE", "NEWS", "README.md")


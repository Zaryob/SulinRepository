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
    shelltools.system("sed -e 's/-Werror//' -i configure.ac")
    autotools.autoreconf("-fiv")
    options="--disable-static"
    if get.buildTYPE()=="emul32":
        options+=" --prefix=/usr --libdir=/usr/lib32"
    else:
        options+=" --prefix=/usr --libdir=/usr/lib"
    shelltools.system("CFLAGS='-fcommon' ./configure "+options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR={}".format(get.installDIR()))
    if get.buildTYPE()=="emul32":
        return


    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

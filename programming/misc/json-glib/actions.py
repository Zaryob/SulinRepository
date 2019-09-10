#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import mesontools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools


def setup():
    mesontools.meson_configure()

def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()
    if get.buildTYPE()=="emul32":
        shelltools.copy("{}/emul32/usr/lib32".format(get.installDIR()),"{}/usr/".format(get.installDIR()))
        #shelltools.copy("{}/emul32/lib32".format(get.installDIR()),"{}/".format(get.installDIR()))
        shelltools.unlinkDir("{}/emul32".format(get.installDIR()))
        shelltools.unlinkDir("{}/usr/usr/".format(get.installDIR()))
        shelltools.unlinkDir("{}/usr/share/installed-tests/".format(get.installDIR()))

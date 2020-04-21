#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


def build():
    autotools.make()

def install():
    shelltools.system('install -d {}/usr/bin'.format(get.installDIR()))
    shelltools.system('install stemwords {}/usr/bin'.format(get.installDIR()))
    shelltools.system('install -d {}/usr/include'.format(get.installDIR()))
    shelltools.system('install include/libstemmer.h {}/usr/include'.format(get.installDIR()))
    shelltools.system('install -d {}/usr/lib'.format(get.installDIR()))
    shelltools.system('install libstemmer.o {}/usr/lib/libstemmer.a'.format(get.installDIR()))

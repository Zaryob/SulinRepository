#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import kde
from inary.actionsapi import get
from inary.actionsapi import shelltools

def setup():
    kde.configure()

def build():
    shelltools.export("LDFLAGS", "{} $(pkg-config libssh2 --libs)".format(get.LDFLAGS()))
    kde.make()

def install():
    kde.install()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2018 Sulin
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def build():
    autotools.make("BINDIR=/bin")


def install():

    autotools.install("DESTDIR=%s install" % get.installDIR())

    inarytools.dodoc("README.md")

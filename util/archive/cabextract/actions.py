#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.make("DESTDIR=%s install" % get.installDIR())


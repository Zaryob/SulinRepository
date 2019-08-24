#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.configure()

def build():
    autotools.make()

def check():
    autotools.make("check -j1")

def install():
    autotools.install()

    inarytools.dohtml("doc/*.html")

    inarytools.remove("/usr/share/doc/gperf.html")

    inarytools.dodoc("AUTHORS", "COPYING", "NEWS", "README")

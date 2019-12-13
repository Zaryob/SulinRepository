#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import inarytools
from inary.actionsapi import kde

# WorkDir = ""
# NoStrip = "/"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    inarytools.dodoc("README*", "MAINTAINER", "TODO")

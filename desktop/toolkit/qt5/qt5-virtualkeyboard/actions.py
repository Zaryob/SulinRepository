#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import qt
from inary.actionsapi import inarytools



def setup():
    qt.configure()

def build():
    qt.make()

def install():
    qt.install()


    inarytools.dodoc("LICENSE.GPL3", "README.md")


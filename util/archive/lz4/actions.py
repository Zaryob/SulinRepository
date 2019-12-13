#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
import os

def build():
    os.system("make -C lib PREFIX=/usr  ")
    os.system("make -C programs lz4 lz4c PREFIX=/usr")

def install():
    os.system("make install")

    inarytools.dodoc("LICENSE", "NEWS", "README.md")

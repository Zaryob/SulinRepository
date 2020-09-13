#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir="Vulkan-Headers-1.2.153"

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release ")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

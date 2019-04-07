#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def build():
    autotools.make()
    autotools.make("busybox.links")

def install():
    inarytools.insinto("/bin", "busybox.links")
    inarytools.insinto("/bin", "busybox")

#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def build():
    autotools.make("allyesconfig")
    autotools.make("toybox")

def install():
    shelltools.system("pwd")
    shelltools.system("mkdir -p {}/bin/".format(get.installDIR()))
    shelltools.system("install toybox {}/bin/toybox".format(get.installDIR()))

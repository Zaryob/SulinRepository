#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def install():
    shelltools.system("cp -prfv {}/mint-themes-1.8.0/files/ {}/".format(get.workDIR(),get.installDIR()))

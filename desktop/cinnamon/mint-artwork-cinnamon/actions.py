#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get



def install():
    shelltools.system('cp -prfv {}/mint-artwork-cinnamon-5.7/ "{}/"'.format(get.workDIR(),get.installDIR()))
    shelltools.system('rm -rf {}/debian'.format(get.installDIR()))


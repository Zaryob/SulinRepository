#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get
#more information : https://gitlab.com/sulinos/inary/tree/master/inary/actionsapi


def build():
    autotools.make("")


def install():
    shelltools.makedirs(get.installDIR()+"/usr/bin/")
    autotools.rawInstall("PREFIX=%s/usr/" % get.installDIR())

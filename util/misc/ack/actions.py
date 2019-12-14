#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def install():
    inarytools.dodir("/usr/bin")
    shelltools.system("install ack-v3.2.0 %s/usr/bin/ack" % get.installDIR())


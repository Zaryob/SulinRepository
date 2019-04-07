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
    shelltools.export("CCACHE_DIR", "%s" % get.workDIR())
    autotools.make('CFLAGS="%s -fno-stack-protector -fno-strict-aliasing"' % get.CFLAGS())

def install():
    inarytools.dobin("disktype")
    inarytools.doman("disktype.1")
    inarytools.dodoc("README", "HISTORY", "TODO")

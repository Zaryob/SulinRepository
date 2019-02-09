#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def build():
    autotools.make('OPT="%s" \
                    SHARED="yes" \
                    PREFIX=/usr \
                    IDSDIR="/usr/share/misc" \
                    all' % get.CFLAGS())

def install():
    autotools.rawInstall('DESTDIR="%s" \
                          PREFIX=/usr \
                          SHARED="yes" \
                          IDSDIR="/usr/share/misc" \
                          install-lib' % get.installDIR())
   
    # remove update-pciids
    inarytools.remove("/usr/sbin/update-pciids")
    inarytools.remove("/usr/share/man/man8/update-pciids.8")


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def build():
    shelltools.export("LDFLAGS", "%s -Wl,-z,now"  % get.LDFLAGS())

#    inarytools.dosed("Makefile", "gcc (\-Wall.*)", "%s \\1 %s" % (get.CC(), get.CFLAGS()))
    inarytools.dosed("Makefile", "^(LDFLAGS[ \t]+=).*", "\\1 %s" % get.LDFLAGS())

    autotools.make()

def install():
    inarytools.doman("crontab.1", "crontab.5", "cron.8")
    inarytools.dodoc("CHANGES", "CONVERSION", "FEATURES", "MAIL", "README", "THANKS")

    inarytools.dosbin("cron")
    inarytools.dobin("crontab")

    inarytools.dodir("/var/spool/cron/crontabs")
    inarytools.dodir("/etc/cron.d")

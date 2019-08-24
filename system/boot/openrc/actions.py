#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

shelltools.export("HOME", get.workDIR())

args = 'BRANDING="Sulin" \
            MKSELINUX=no \
            MKTERMCAP=ncurses \
            PKG_PREFIX=""\
            LIBDIR=/usr/lib \
            SHLIBDIR=/usr/lib \
            LIBEXECDIR=/usr/lib/openrc \
            BINDIR=/usr/bin \
            SBINDIR=/sbin \
	    INCLUDEDIR=/usr/include \
            SYSCONFDIR=/etc'


def build():
    autotools.make("%s"% args)

def install():
    autotools.rawInstall("DESTDIR=%s %s" % (get.installDIR(),args))

    inarytools.insinto("/etc", "support/sysvinit/inittab")

    inarytools.dodoc("LICENSE*", "*guide.*", "AUTHORS", "ChangeLog", "README.*")

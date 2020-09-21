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
            MKBASHCOMP=yes \
            MKSELINUX=no \
            MKTERMCAP=ncurses \
            MKZSHCOMP=yes\
            PKG_PREFIX=""\
            LIBDIR=/usr/lib \
            SHLIBDIR=/usr/lib \
            LIBEXECDIR=/usr/libexec/openrc \
            BINDIR=/usr/bin \
            SBINDIR=/sbin \
            INCLUDEDIR=/usr/include \
            SYSCONFDIR=/etc'


def build():
    autotools.make("%s"% args)

def install():
    autotools.install("DESTDIR=%s %s" % (get.installDIR(),args))
    
    inarytools.dodoc("LICENSE*", "*guide.*", "AUTHORS", "ChangeLog", "README.*")

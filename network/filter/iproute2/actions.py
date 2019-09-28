#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make('CC="%s" RPM_OPT_FLAGS="%s"' % (get.CC(), get.CFLAGS()))

def install():
    autotools.rawInstall("DESTDIR=\"%s\" \
                          SBINDIR=/sbin \
                          DOCDIR=/%s/%s \
                          MANDIR=/usr/share/man \
                          " % (get.installDIR(), get.docDIR(), get.srcNAME()))

    inarytools.dodir("/var/lib/arpd")

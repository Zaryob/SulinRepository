#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

makeargs="prefix=/usr sbindir=/usr/bin mandir=/usr/share/man SYS=posix CRYPTO=GNUTLS"

def build():

    autotools.make(makeargs, )

def install():
    autotools.rawInstall(' -j1 %s DESTDIR=%s' % (makeargs, get.installDIR()))

    inarytools.insinto("/usr/share/doc/%s" % get.srcNAME(), "librtmp/COPYING", "librtmp-COPYING")
    inarytools.dodoc("COPYING", "ChangeLog", "README")
